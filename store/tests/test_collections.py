from rest_framework import status
import pytest


def create_collection(api_client):
    def do_create_collection(collection):
        return api_client.post('/store/collections/', collection)
    return do_create_collection
        

@pytest.mark.django_db    
class TestCreateCollection:
    def test_if_user_is_annonymous_returns_401(self, create_collection):
        #AAA(Arrange, Act, Assert)
        response = create_collection({'title': 'a'})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED  
        
    def test_if_user_is_not_admin_returns_403(self, api_client, create_collection):
        api_client.force_authenticate(user={})
        response = create_collection({'title': 'a'})
        assert response.status_code == status.HTTP_403_FORBIDDEN      