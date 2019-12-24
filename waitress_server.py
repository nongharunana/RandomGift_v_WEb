from waitress import serve
import random_product
serve(random_product.app, host='0.0.0.0', port=8080)