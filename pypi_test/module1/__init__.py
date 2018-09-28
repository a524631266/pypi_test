name = "module1"
import cmd
import subprocess

class CLI(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = 'zhangll test>'
    def do_shell(self,arg):
        "run a shell command"
        print(">>>",arg)
        sub_cmd = subprocess.Popen(arg, shell=True, stdout=subprocess.PIPE)
        print(sub_cmd.communicate()[0])
def runcmd():
    cli = CLI()
    cli.cmdloop()