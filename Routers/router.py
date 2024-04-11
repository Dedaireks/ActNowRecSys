from fastapi import APIRouter


from Routers import user, post, stories, auth

router = APIRouter()

router.include_router(user.router, prefix='', tags=['user'])
router.include_router(post.router, prefix='/post', tags=['post'])
router.include_router(stories.router, prefix='', tags=['stories'])
router.include_router(auth.router, prefix='', tags=['auth'])
