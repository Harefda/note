from rest_framework.request import Request


def get_body_data(request: Request, required_fields: list[str]) -> dict:
    data = request.POST or request.data
    response_data = {}
    for field in required_fields:
        try:
            response_data[field] = data[field]
        except KeyError:
            raise KeyError(f"Field - {field} is required")

    return response_data
