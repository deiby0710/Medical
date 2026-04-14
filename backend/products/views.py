from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product
import json

# =========================
# GET: Obtener todos los productos
# =========================
def get_products(request):
    if request.method == 'GET':
        products = list(Product.objects.values())
        
        if not products:
            return JsonResponse({'message': 'No products found'}, status=404)
        
        return JsonResponse(products, safe=False)


# =========================
# GET: Obtener producto por ID
# =========================
def get_product_by_id(request, id):
    try:
        product = Product.objects.get(id=id)
        return JsonResponse({
            'id': product.id,
            'comercial_name': product.comercial_name,
            'generic_name': product.generic_name,
            'quantity': product.quantity,
            'lote': product.lote,
            'price': float(product.price),
            'description': product.description,
            'pharmaceutic_form': product.pharmaceutic_form,
            'cum': product.cum,
            'final_date': product.final_date
        })
    except Product.DoesNotExist:
        return JsonResponse({'message': 'Product not found'}, status=404)


# =========================
# GET: Buscar por nombre
# =========================
def get_product_by_name(request, name):
    products = Product.objects.filter(comercial_name__icontains=name).values()

    if not products:
        return JsonResponse({'message': 'No products found'}, status=404)

    return JsonResponse(list(products), safe=False)


# =========================
# POST: Crear producto
# =========================
@csrf_exempt
def create_product(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        try:
            product = Product.objects.create(
                comercial_name=data.get('comercial_name'),
                generic_name=data.get('generic_name'),
                quantity=data.get('quantity'),
                lote=data.get('lote'),
                price=data.get('price'),
                description=data.get('description'),
                pharmaceutic_form=data.get('pharmaceutic_form'),
                cum=data.get('cum'),
                final_date=data.get('final_date')
            )

            return JsonResponse({'message': 'Product created', 'id': product.id})
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


# =========================
# PUT: Actualizar producto
# =========================
@csrf_exempt
def update_product(request, id):
    if request.method == 'PUT':
        try:
            product = Product.objects.get(id=id)
            data = json.loads(request.body)

            product.comercial_name = data.get('comercial_name')
            product.generic_name = data.get('generic_name')
            product.quantity = data.get('quantity')
            product.lote = data.get('lote')
            product.price = data.get('price')
            product.description = data.get('description')
            product.pharmaceutic_form = data.get('pharmaceutic_form')
            product.cum = data.get('cum')
            product.final_date = data.get('final_date')

            product.save()

            return JsonResponse({'message': 'Product updated'})
        
        except Product.DoesNotExist:
            return JsonResponse({'message': 'Product not found'}, status=404)


# =========================
# DELETE: Eliminar producto
# =========================
@csrf_exempt
def delete_product(request, id):
    if request.method == 'DELETE':
        try:
            product = Product.objects.get(id=id)
            product.delete()

            return JsonResponse({'message': 'Product deleted'})
        
        except Product.DoesNotExist:
            return JsonResponse({'message': 'Product not found'}, status=404)