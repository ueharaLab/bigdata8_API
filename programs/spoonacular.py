



import spoonacular
from spoonacular.models.search_recipes_by_ingredients200_response_inner import SearchRecipesByIngredients200ResponseInner
from spoonacular.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.spoonacular.com
# See configuration.py for a list of all supported configuration parameters.
configuration = spoonacular.Configuration(
    host = "https://api.spoonacular.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
API_KEY = '46dc84a07678488ba464a0e62b7680d8'
# Configure API key authorization: apiKeyScheme
configuration.api_key['apiKeyScheme'] = os.environ[API_KEY]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyScheme'] = 'Bearer'

# Enter a context with an instance of the API client
with spoonacular.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spoonacular.RecipesApi(api_client)
    ingredients = 'carrots,tomatoes' # str | A comma-separated list of ingredients that the recipes should contain.
    number = 10 # int | The maximum number of items to return (between 1 and 100). Defaults to 10. (optional) (default to 10)
    ranking = 1 # int | Whether to maximize used ingredients (1) or minimize missing ingredients (2) first. (optional)
    ignore_pantry = False # bool | Whether to ignore typical pantry items, such as water, salt, flour, etc. (optional) (default to False)

    try:
        # Search Recipes by Ingredients
        api_response = api_instance.search_recipes_by_ingredients(ingredients, number=number, ranking=ranking, ignore_pantry=ignore_pantry)
        print("The response of RecipesApi->search_recipes_by_ingredients:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecipesApi->search_recipes_by_ingredients: %s\n" % e)