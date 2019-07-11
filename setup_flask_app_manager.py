# coding=utf-8
import os


def main():
    if not os.path.isdir("/www"):
        os.makedirs("/www")

    # 检查 caddy 是否已经被安装
    if not os.path.isfile("/usr/local/bin/caddy"):
        # 若没有，则执行安装脚本
        os.system("curl https://getcaddy.com | bash -s personal")
    
    # 再次检查
    if not os.path.isfile("/usr/local/bin/caddy"):
        # 终止
        print("failed to install caddyserver")
        return

    app_dir = "/www/flask_app_manager"
    
    # 拉取代码
    os.system("yum -y install git")
    os.system("git clone https://github.com/hechenggang/flask_app_manager.git {}".format(app_dir))

    # 创建虚拟环境
    venv_path = os.path.join(app_dir, "venv")
    os.makedirs(venv_path)
    os.system("python3.7 -m venv {}".format(venv_path))
    os.system("{} install -r {} -i https://pypi.tuna.tsinghua.edu.cn/simple/".format(
            os.path.join(app_dir, "venv", "bin", "pip3.7"), 
            os.path.join(app_dir, "requirements.txt")
        ))
    
    print("finish")

if __name__ == "__main__":
    main()