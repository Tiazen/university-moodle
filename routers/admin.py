from fastapi import APIRouter


router = APIRouter(
    prefix='/admin',
    tags=['admin'],
    responses={404: {'description': 'Not found'}}
)


@router.get('/users')
def get_all_users():
    return {'test': 'test'}