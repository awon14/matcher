# %%
from pathlib import Path
from rest_framework.permissions import IsAuthenticated
import torch
from sentence_transformers import util
from rest_framework.decorators import api_view, permission_classes

from . serializers import request_serializer, results_serializer
from rest_framework.response import Response
from . apps import ApiConfig


# %%

embedder = ApiConfig.embedder

corpus = ApiConfig.corpus
corpus_embeddings = ApiConfig.corpus_embeddings
commands = ApiConfig.commands

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def match(request):
    if request.method == 'POST':

        ser = request_serializer(data=request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            req_id = ser.data["id"]
            query = request.data['query']

            # Find the closest 5 sentences of the corpus for each query sentence based on cosine similarity
            top_k = min(5, len(corpus))
            query_embedding = embedder.encode(query, convert_to_tensor=True)

            # We use cosine-similarity and torch.topk to find the highest 5 scores
            cos_scores = util.cos_sim(query_embedding, corpus_embeddings)[0]
            top_results = torch.topk(cos_scores, k=top_k)

            print("\n\n======================\n\n")
            print("Query:", query)
            print("\nTop 5 most similar sentences in corpus:")

            matched = []
            scores = []
            cmds = []
            for score, idx in zip(top_results[0], top_results[1]):
                print(corpus[idx], "(Score: {:.4f})".format(score))
                matched.append(corpus[idx])
                scores.append(score)
                cmds.append(commands[idx])
                # save to database
                ser_ = results_serializer(data={
                    "query_id": str(req_id),
                    "matched": str(corpus[idx]),
                    "scores": str(score),
                    "commands": str(commands[idx])})
                if ser_.is_valid(raise_exception=True):
                    ser_.save()

            return Response({"cmd_input":query,"matched": matched, "scores": scores, "commands" : cmds})
