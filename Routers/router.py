from fastapi import APIRouter


from Routers import user, post, stories, auth, vk_auth, complaints,tags

router = APIRouter()

router.include_router(user.router, prefix='/user', tags=['user'])
router.include_router(post.router, prefix='/post', tags=['post'])
router.include_router(stories.router, prefix='/stories', tags=['stories'])
router.include_router(auth.router, prefix='/auth', tags=['auth'])
router.include_router(complaints.router, prefix="/complaint", tags=['complaints'])
router.include_router(tags.router, prefix="/tag", tags=['tags'])
# router.include_router(vk_auth.router, prefix='', tags=['vk'])
