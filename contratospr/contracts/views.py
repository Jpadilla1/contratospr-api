import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

from .models import Contract, Contractor, Document, Entity
from .tasks import detect_text


def index(request):
    entities = Entity.objects.all()
    context = {"entities": entities}
    return render(request, "contracts/entities.html", context)


def entity(request, entity_id):
    entity = get_object_or_404(Entity, pk=entity_id)
    context = {"entity": entity}
    return render(request, "contracts/entity.html", context)


def contract(request, contract_id):
    contract = get_object_or_404(Contract, pk=contract_id)
    context = {"contract": contract}
    return render(request, "contracts/contract.html", context)


def contractor(request, contractor_id):
    contractor = get_object_or_404(Contractor, pk=contractor_id)
    context = {"contractor": contractor}
    return render(request, "contracts/contractor.html", context)


@csrf_exempt
def filepreviews_webhook(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body.decode("utf8"))
            document_id = body["user_data"]["document_id"]

            if document_id:
                Document.objects.filter(pk=document_id).update(preview_data=body)
                detect_text.send(document_id)
                return JsonResponse({"success": True}, status=200)

        except Exception:
            pass

    return JsonResponse({"success": False}, status=400)
