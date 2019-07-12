# coding=utf-8
import os


def install():
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

    # 检查 python3.7 是否已经被安装
    if not os.path.isfile("/usr/bin/python3.7"):
        # 若没有，则执行安装脚本
        os.system("curl https://raw.githubusercontent.com/hechenggang/i_love_linux/master/install-python.sh | bash install-python.sh")
    
    # 再次检查
    if not os.path.isfile("/usr/bin/python3.7"):
        # 终止
        print("failed to install python3.7")
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
    
    # 创建 caddy 进程，两个（一个为主程序服务，一个为平台上的应用程序服务）
    # 创建 flask_app_manager 进程
    os.system("cp {}/config_file/daemon/caddy/caddy_for_app.service /etc/systemd/system/caddy_for_app.service".format(app_dir))
    os.system("cp {}/config_file/daemon/caddy/caddy_for_flask_app_manager.service /etc/systemd/system/caddy_for_flask_app_manager.service".format(app_dir))
    os.system("cp {}/config_file/daemon/flask_app_manager/flask_app_manager.service /etc/systemd/system/flask_app_manager.service".format(app_dir))
    os.system("systemctl daemon-reload")
    os.system("systemctl start flask_app_manager && systemctl enable flask_app_manager")
    os.system("systemctl start caddy_for_flask_app_manager && systemctl enable caddy_for_flask_app_manager")
    os.system("systemctl start caddy_for_app && systemctl enable caddy_for_app")
    

    print("finish")


def uninstall():
    app_dir = "/www/flask_app_manager"
    os.system("rm -rf {}".format(app_dir))
    if not os.path.isdir(app_dir):
        os.makedirs(app_dir)
    d1 = "/etc/systemd/system/caddy_for_app.service"
    d2 = "/etc/systemd/system/caddy_for_flask_app_manager.service"
    d3 = "/etc/systemd/system/flask_app_manager.service"
    for i in [d1,d2,d3]:
        if os.path.isfile(i):
            os.system("rm -rf {}".format(i))
            name = os.path.split(i)[1].replace(".service","")
            os.system("systemctl start {} && systemctl enable {}".format(name,name))

    print("finish")

def main():
    try: 
        get_answer = raw_input
    except NameError: 
        get_answer = input
    print("1 INSTALL")
    print("2 UNINSTALL")
    a = int(get_answer("INPUT NUMBER OF CHOOSE: "))
    print(a)
    if a == 1:
        c = str(get_answer("DO YOU WANT TO INSTALL ? (Y/N)"))
        if c == "Y":
            install()
        else:
            print("CANCELED")
    elif a == 2:
        
        c = str(get_answer("DO YOU WANT TO UNINSTALL ? (Y/N)"))
        if c == "Y":
            uninstall()
        else:
            print("CANCELED")

if __name__ == "__main__":
    main()