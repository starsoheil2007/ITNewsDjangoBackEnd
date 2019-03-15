from rest_framework import status
from rest_framework.response import Response


def create_response(success, message, code, error_code, item, list_item):
    data = dict()
    data['ErrorCode'] = error_code

    if code == 200:
        data['IsSuccess'] = success
        data['Message'] = message
        data['Item'] = item
        data['ListItems'] = list_item
        return Response(data=data, status=status.HTTP_200_OK)
    elif code == 401:
        data['IsSuccess'] = False
        data['Message'] = 'Authentication Failed : ' + message
        data['Item'] = None
        data['ListItems'] = None
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)
    elif code == 403:
        data['IsSuccess'] = False
        data['Message'] = 'FORBIDDEN'
        data['Item'] = None
        data['ListItems'] = None
        return Response(data=data, status=status.HTTP_403_FORBIDDEN)
    elif code == 404:
        data['IsSuccess'] = False
        data['Message'] = message
        data['Item'] = None
        data['ListItems'] = None
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)
    elif code == 400:
        data['IsSuccess'] = False
        data['Message'] = message
        data['Item'] = item
        data['ListItems'] = None
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
