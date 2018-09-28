name = "module1"
import cmd
import subprocess

class CLI(cmd.Cmd):
    """
        Cmd 使用方法
        比如想要在交互环境中输入 hello arg1 这样的指令
        只要在继承了Cmd的类中定义 do_hello就可以了
        方式为
            def do_hello1():
                print("hello")

            eval('do_'+'hello1')()
    """
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = 'zhangll test>'
    def do_shell(self,arg):
        "run a shell command"
        print(">>>",arg)
        sub_cmd = subprocess.Popen(arg, shell=True, stdout=subprocess.PIPE)
        print(sub_cmd.communicate()[0])
    def do_hello(self,arg1):
        print(">>>>","welcome"+ arg1)

def runcmd():
    cli = CLI()
    cli.cmdloop()
