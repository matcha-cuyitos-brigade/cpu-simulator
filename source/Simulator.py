from SoC import *
from flask import Flask, request #import main Flask class and request object
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


@app.route("/boot_ui")
def boot_ui():
    visualization_options = my_soc.boot()
    boot_json = {
        "register1": my_soc.cpu.register_a,
        "register2": my_soc.cpu.register_b,
        "register3": my_soc.cpu.register_c,
        "register4": my_soc.cpu.register_d,
        "RAM0": my_soc.ram.ram_array[0],
        "RAM1": my_soc.ram.ram_array[1],
        "RAM2": my_soc.ram.ram_array[2],
        "RAM3": my_soc.ram.ram_array[3],
        "RAM4": my_soc.ram.ram_array[4],
        "RAM5": my_soc.ram.ram_array[5],
        "RAM6": my_soc.ram.ram_array[6],
        "RAM7": my_soc.ram.ram_array[7],
        "RAM8": my_soc.ram.ram_array[8],
        "RAM9": my_soc.ram.ram_array[9],
        "RAM10": my_soc.ram.ram_array[10],
        "RAM11": my_soc.ram.ram_array[11],
        "RAM12": my_soc.ram.ram_array[12],
        "RAM13": my_soc.ram.ram_array[13],
        "RAM14": my_soc.ram.ram_array[14],
        "RAM15": my_soc.ram.ram_array[15],
        "clock": my_soc.cpu.cu.clock,
        "RAM_cuyo": visualization_options[0],
        "registers_cuyo": visualization_options[1],
        "clock_cuyo": visualization_options[2],
        "ALU_cuyo": visualization_options[3],
    }

    x = json.dumps(boot_json)
    return x

@app.route("/run_ui", methods=['GET', 'POST']) #allow both GET and POST requests
def run_ui():
    if request.method == 'POST':  # this block is only entered when the form is submitted


my_soc = SoC()
my_soc.run()
if __name__ == "__main__":
    app.run(host="0.0.0.0")
