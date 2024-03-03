import os
import subprocess
import time
from colablib.colored_print import cprint, print_line

if 'content' in os.listdir('/'):
    ui = "/content"
    env = 'Colab'
elif 'kaggle' in os.listdir('/'):
    ui = "/kaggle/working"
    env = 'Kaggle'
else:
     cprint('Error. Enviroment not detected', color="flat_red")
    
branch = "master"
ui_path = os.path.join(ui, "x1101")
git_path = os.path.join(ui_path, "extensions")

def kontolondon(oppai, asu, si_kontol, kntl, debug=True):   
    start_time = time.time() 
    cprint(f"    > {asu}", color="flat_cyan")
    try:
        #subprocess.run(oppai, check=True, shell=True, text=True)  # for debug
        subprocess.run(oppai, check=True, shell=True, text=True,  stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        si_kontol += 1
    except subprocess.CalledProcessError as e:
        print(f"Error at [{asu}]: {e}")
        kntl += 1
    end_time = time.time()
    return si_kontol, kntl, end_time - start_time

if __name__ == "__main__":
    rudi = [
        ("apt -y install aria2", "aria2"),
        ("apt-get install lz4", "lz4"),
        ("pip install colorama", "colorama"),
        ("npm install -g localtunnel", "localtunnel"),
        ("curl -s -OL https://github.com/DEX-1101/sd-webui-notebook/raw/main/res/new_tunnel", "new_tunnel"),
        ("curl -s -Lo /usr/bin/cl https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 && chmod +x /usr/bin/cl", "cloudflared"),
        (f"curl -sLO https://github.com/openziti/zrok/releases/download/v0.4.23/zrok_0.4.23_linux_amd64.tar.gz && tar -xzf zrok_0.4.23_linux_amd64.tar.gz && rm -rf zrok_0.4.23_linux_amd64.tar.gz && mv {ui}/zrok /usr/bin", "zrok"),
        (f"wget https://github.com/gutris1/segsmaker/raw/main/kaggle/script/pantat88.py -O {ui}/semvak_zeus.py", "semvak_zeus.py")
    ]

    yanto = [
        (f"wget https://raw.githubusercontent.com/DEX-1101/SecretNAI/main/template.txt -O {ui}/download_list.txt", "download_list.txt"),
        (f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/x1101/UI/resolve/main/ui.tar.lz4 -o ui.tar.lz4 && tar -xI lz4 -f ui.tar.lz4 && mv {ui}/kaggle/working/x1101 {ui} && rm {ui}/ui.tar.lz4 && rm -rf {ui}/kaggle", "Installing UI..."),
        (f"cd {ui_path} && git reset --hard && git pull && git switch {branch} && git pull && git reset --hard", "Updating UI..."),
        (f"find {git_path} -mindepth 1 -maxdepth 1 -type d -print -exec git -C {{}} reset --hard \;", "Updating Extensions...")
        
    ]

    agus = []
    
    if 'content' in os.listdir('/'):
        agus.append(("pip install xformers==0.0.22.post7", "Installing xformers..."))
    elif 'kaggle' in os.listdir('/'):
        agus.append(("pip install torch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2", "Installing torch..."))
        agus.append(("pip install xformers==0.0.23.post1", "Installing xformers..."))
    else:
        agus.append((""))
            
    si_kontol = 0
    kntl = 0
    total_time = 0
    
    cprint(f"[+] Installing [{env}] Requirments", color="flat_yellow")
    for oppai, asu in rudi + yanto + agus:
        si_kontol, kntl, command_time = kontolondon(oppai, asu, si_kontol, kntl)
        total_time += command_time
        
    print_line(0)
    cprint(f"[+] {kntl} of {si_kontol} error found. All completed within: {total_time:.2f} secs", color="flat_yellow")
