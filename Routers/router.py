from fastapi import APIRouter


from Routers import user, post, stories, auth, vk_auth, complaints,tags

router = APIRouter()

router.include_router(user.router, prefix='', tags=['user'])
router.include_router(post.router, prefix='/post', tags=['post'])
router.include_router(stories.router, prefix='', tags=['stories'])
router.include_router(auth.router, prefix='', tags=['auth'])
router.include_router(complaints.router, prefix="", tags=['complaints'])
router.include_router(tags.router, prefix="", tags=['tags'])
# router.include_router(vk_auth.router, prefix='', tags=['vk'])
