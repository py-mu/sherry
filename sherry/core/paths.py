# coding=utf-8
"""
    create by pymu
    on 2021/6/20
    at 17:11
"""
import os

__class_path__ = os.path.abspath(os.path.dirname(__file__))  # Note: config 模块文件路径 (the config file path)

__package_path__ = os.path.abspath(os.path.join(__class_path__, os.path.pardir))

__project_path__ = os.getcwd()  # Note: 项目路径(project path)


class SherryPath:
    """
        内部路径配置类

        The default path configuration of the Sherry.
    """

    @classmethod
    def path_exists(cls, path):
        """
        判断路径是否存在

        Return whether the path exists.
        :param path: 路径
        """
        return os.path.exists(path)

    @classmethod
    def path_create(cls, path):
        """
        创建路径,并返回

        Create if it doesn't exist.

        :param path:
        :return:
        """
        if not cls.path_exists(path) and '.' not in path:
            os.makedirs(path)
        return path

    @classmethod
    def link(cls, source, target, create=False):
        """
        :param create: 不存在创建(create or not)
        :param source: 上级路径
        :param target: 连接路径
        """
        path = os.path.join(source, target)
        if create:
            cls.path_create(path)
        return path

    @property
    def package_path(self):
        """
        框架根路径

        The path of Sherry site-package
        """
        return __package_path__

    @property
    def package_resource_path(self):
        """
        返回pip包内的image文件路径

        Return the Sherry resource path in the site-package.
        """
        return self.link(self.package_path, "resource")

    @property
    def package_qss_path(self):
        """
        返回pip包内的静态资源qss文件路径（在项目没有可调用的qss时查询包内自带的qss样式）

        Return the Sherry qss path in the site-package.
        """
        return self.link(self.package_resource_path, "qss")

    @property
    def package_img_path(self):
        """
        返回pip内的静态文件img路径（在没有项目资源路径时调用包内资源）

        Return the Sherry image path in the site-package.
        """
        return self.link(self.package_resource_path, "img")

    @property
    def package_font_path(self):
        """
        返回包内的静态文件font的路径

        Return the Sherry font path in the site-package.
        """
        return self.link(self.package_resource_path, 'font')

    @property
    def project_path(self):
        """
        项目路径

        The path of project
        """
        return __project_path__

    @property
    def project_resource_path(self):
        """
        资源文件夹, 当路径不存在时会创建

        The resource path of the project,
        The path will be created if it does not exist.
        """
        return self.link(self.project_path, "resource")

    @property
    def project_img_path(self):
        """
        默认的图片资源文件夹

        The image path of the project
        """
        return self.link(self.project_resource_path, "img")

    @property
    def project_font_path(self):
        """
        返回包内的静态文件font的路径

        The font path of the project.
        """
        return self.link(self.project_resource_path, 'font')

    @property
    def project_qss_path(self):
        """
        样式文件夹

        The qss path of the project
        """
        return self.link(self.project_resource_path, "qss")

    @property
    def log_path(self):
        """
        默认的日志文件夹

        Default log path of the project.
        The path will be created if it does not exist.
        """
        return self.link(self.project_path, "log", create=True)

    @property
    def user_desktop(self):
        """
        返回桌面

        Return the path of user desktop.
        """
        return self.link(self.user_home, "Desktop")

    @property
    def user_home(self):
        """
        返回用户目录

        Return the path of user home.
        """
        return os.path.expanduser('~')

    def file_path(self, file_name):
        """
        读取json文件, 如果工程中不存在则访问包路径的文件

         read json file from  package or project
        """
        path = self.link(self.project_resource_path, file_name)
        if not self.path_exists(path):
            path = self.link(self.package_resource_path, file_name)
        return path

    def get_path_in(self, *args, name):
        """获取路径， 根据顺序依次查找，如果没有则返回None， 如果不指定不定长参数则返回文件名"""
        if not args:
            return name
        for root in args:
            path = self.link(root, name)
            if self.path_exists(path):
                return path
        return None
