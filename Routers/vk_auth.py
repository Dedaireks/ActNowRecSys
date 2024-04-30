# from fastapi import APIRouter, Request, HTTPException
# from Services.vk.auth import get_vk_auth_url, gev_vk_access_token
#
#
# client_id = "51901205"
# redirect_url = "https://actnow.com"  # ссылка нужна нормальная
# protected_key = "MT3X7owJ2WODFv7YtlZR"
# client_secret = ""
#
# router = APIRouter()
#
#
# @router.get("/vk_auth")
# async def vk_auth_redirect(request: Request):
#     code = request.query_params.get("code")
#     if code is None:
#         raise HTTPException(
#             status_code=400,
#             detail="Code not provided",
#         )
#     else:
#         access_token_info = gev_vk_access_token(client_id, client_secret, redirect_url, code)
#         return access_token_info
#
#
# @router.get("/vk_auth_url")
# async def vk_auth_url():
#     url = get_vk_auth_url(client_id, redirect_url)
#     return {"url": url}