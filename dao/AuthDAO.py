from .BaseDAO import BaseDAO
from mapper.AuthDO import AuthDO
from mapper.RoleAuthsDO import RoleAuthsDO


class AuthDAO(BaseDAO):
    """ 权限相关原子操作 """
    def get_auths(self):
        """ 获取所有auth """
        return self.session.query(AuthDO).all()

    def add_auth(self, auth):
        self.session.add(auth)
        self.session.flush()

    def get_auth_by_code(self, code=None):
        """ 根据code获取auth """
        return self.session.query(AuthDO).filter(AuthDO.code == code).first()

    def have_power(self, roles=[], auth_id=None):
        """ 判断角色是否有指定权限 """
        return self.session.query(RoleAuthsDO).filter(RoleAuthsDO.role.in_(roles), RoleAuthsDO.auth_id == auth_id).first()
