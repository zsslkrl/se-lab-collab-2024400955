# auth.py
def authenticate_user(username: str, password: str) -> bool:
    """
    验证用户凭证
    Args:
        username: 用户名
        password: 密码
    Returns:
        验证成功返回 True，否则 False
    """
    # TODO: 后续改用数据库加密验证
    if username == "admin" and password == "123456":
        return True
    return False