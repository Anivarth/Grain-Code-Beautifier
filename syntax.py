from flask import Flask,request,render_template, send_from_directory,Markup
from pygments.lexers import get_all_lexers
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

app = Flask(__name__)

@app.route('/static/<path:filename>')
def send_img(filename):
    return send_from_directory('static', filename)

@app.route('/')
def hl():
	return render_template('index.html')

@app.route('/',methods=['POST','GET'])
def high():
	code = request.form['code']
	programming_language = request.form['language']
	lexer = get_lexer_by_name(str(programming_language))
	font_size = request.form['font_size']
	style = request.form['style']
	formatter = HtmlFormatter(cssclass=style)
	css = HtmlFormatter(style=style).get_style_defs('.'+style)
	code_highlighted = highlight(code,lexer,formatter)
	style_css = {'manni': '.manni .cs,.manni .gh,.manni .gp,.manni .gs,.manni .gu,.manni .k,.manni .kc,.manni .kd,.manni .kn,.manni .kt,.manni .nc,.manni .ne,.manni .ni,.manni .nn,.manni .nt,.manni .ow,.manni .se{font-weight:700}.manni .hll{background-color:#ffc}.manni{background:#f0f3f3}.manni .c{color:#09F;font-style:italic}.manni .err{color:#A00;background-color:#FAA}.manni .k{color:#069}.manni .o{color:#555}.manni .cm{color:#09F;font-style:italic}.manni .cp{color:#099}.manni .c1,.manni .cs{color:#09F;font-style:italic}.manni .gd{background-color:#FCC;border:1px solid #C00}.manni .ge{font-style:italic}.manni .gr{color:red}.manni .gh{color:#030}.manni .gi{background-color:#CFC;border:1px solid #0C0}.manni .go{color:#AAA}.manni .gp{color:#009}.manni .gu{color:#030}.manni .gt{color:#9C6}.manni .kc,.manni .kd,.manni .kn,.manni .kp,.manni .kr{color:#069}.manni .kr{font-weight:700}.manni .kt{color:#078}.manni .m{color:#F60}.manni .s{color:#C30}.manni .na{color:#309}.manni .nb{color:#366}.manni .nc{color:#0A8}.manni .no{color:#360}.manni .nd{color:#99F}.manni .ni{color:#999}.manni .ne{color:#C00}.manni .nf{color:#C0F}.manni .nl{color:#99F}.manni .nn{color:#0CF}.manni .nt{color:#309}.manni .nv{color:#033}.manni .ow{color:#000}.manni .w{color:#bbb}.manni .mb,.manni .mf,.manni .mh,.manni .mi,.manni .mo{color:#F60}.manni .s2,.manni .sb,.manni .sc,.manni .sd,.manni .se,.manni .sh{color:#C30}.manni .sd{font-style:italic}.manni .si{color:#A00}.manni .sx{color:#C30}.manni .sr{color:#3AA}.manni .s1{color:#C30}.manni .ss{color:#FC3}.manni .bp{color:#366}.manni .vc,.manni .vg,.manni .vi{color:#033}.manni .il{color:#F60}', 'igor': '.igor .hll{background-color:#ffc}.igor{background:#fff}.igor .c{color:red;font-style:italic}.igor .k{color:#00F}.igor .c1,.igor .cm,.igor .cp,.igor .cs{color:red;font-style:italic}.igor .kc,.igor .kd,.igor .kn,.igor .kp,.igor .kr,.igor .kt{color:#00F}.igor .s{color:#009C00}.igor .nc{color:#007575}.igor .nd{color:#CC00A3}.igor .nf{color:#C34E00}.igor .s1,.igor .s2,.igor .sb,.igor .sc,.igor .sd,.igor .se,.igor .sh,.igor .si,.igor .sr,.igor .ss,.igor .sx{color:#009C00}', 'xcode': '.xcode .hll{background-color:#ffc}.xcode{background:#fff}.xcode .c{color:#177500}.xcode .err{color:#000}.xcode .k{color:#A90D91}.xcode .l{color:#1C01CE}.xcode .n,.xcode .o{color:#000}.xcode .cm{color:#177500}.xcode .cp{color:#633820}.xcode .c1,.xcode .cs{color:#177500}.xcode .kc,.xcode .kd,.xcode .kn,.xcode .kp,.xcode .kr,.xcode .kt{color:#A90D91}.xcode .ld,.xcode .m{color:#1C01CE}.xcode .s{color:#C41A16}.xcode .na{color:#836C28}.xcode .nb{color:#A90D91}.xcode .nc{color:#3F6E75}.xcode .nd,.xcode .ne,.xcode .nf,.xcode .ni,.xcode .nl,.xcode .nn,.xcode .no,.xcode .nt,.xcode .nv,.xcode .nx,.xcode .ow,.xcode .py{color:#000}.xcode .mb,.xcode .mf,.xcode .mh,.xcode .mi,.xcode .mo{color:#1C01CE}.xcode .sb{color:#C41A16}.xcode .sc{color:#2300CE}.xcode .s1,.xcode .s2,.xcode .sd,.xcode .se,.xcode .sh,.xcode .si,.xcode .sr,.xcode .ss,.xcode .sx{color:#C41A16}.xcode .bp{color:#5B269A}.xcode .vc,.xcode .vg,.xcode .vi{color:#000}.xcode .il{color:#1C01CE}', 'vim': '.vim .cs,.vim .gh,.vim .gp,.vim .gs,.vim .gu,.vim .ne{font-weight:700}.vim .hll{background-color:#222}.vim{background:#000;color:#ccc}.vim .c{color:navy}.vim .err,.vim .esc,.vim .g{color:#ccc}.vim .err{border:1px solid red}.vim .k{color:#cdcd00}.vim .l,.vim .n{color:#ccc}.vim .o{color:#39c}.vim .p,.vim .x{color:#ccc}.vim .c1,.vim .cm,.vim .cp{color:navy}.vim .cs,.vim .gd{color:#cd0000}.vim .ge{color:#ccc;font-style:italic}.vim .gr{color:red}.vim .gh{color:navy}.vim .gi{color:#00cd00}.vim .go{color:#888}.vim .gp{color:navy}.vim .gs{color:#ccc}.vim .gu{color:purple}.vim .gt{color:#04D}.vim .kc{color:#cdcd00}.vim .kd{color:#00cd00}.vim .kn{color:#cd00cd}.vim .kp,.vim .kr{color:#cdcd00}.vim .kt{color:#00cd00}.vim .ld{color:#ccc}.vim .m{color:#cd00cd}.vim .s{color:#cd0000}.vim .na{color:#ccc}.vim .nb{color:#cd00cd}.vim .nc{color:#00cdcd}.vim .nd,.vim .ni,.vim .no{color:#ccc}.vim .ne{color:#669}.vim .nf,.vim .nl,.vim .nn,.vim .nt,.vim .nx,.vim .py{color:#ccc}.vim .nv{color:#00cdcd}.vim .ow{color:#cdcd00}.vim .w{color:#ccc}.vim .mb,.vim .mf,.vim .mh,.vim .mi,.vim .mo{color:#cd00cd}.vim .s1,.vim .s2,.vim .sb,.vim .sc,.vim .sd,.vim .se,.vim .sh,.vim .si,.vim .sr,.vim .ss,.vim .sx{color:#cd0000}.vim .bp{color:#cd00cd}.vim .vc,.vim .vg,.vim .vi{color:#00cdcd}.vim .il{color:#cd00cd}', 'autumn': '.autumn .c,.autumn .c1,.autumn .cm,.autumn .cs,.autumn .ge{font-style:italic}.autumn .nc,.autumn .nn{text-decoration:underline}.autumn .gh,.autumn .gs,.autumn .gu,.autumn .ni,.autumn .nt{font-weight:700}.autumn .hll{background-color:#ffc}.autumn{background:#fff}.autumn .c{color:#aaa}.autumn .err{color:red;background-color:#FAA}.autumn .k{color:#00a}.autumn .cm{color:#aaa}.autumn .cp{color:#4c8317}.autumn .c1{color:#aaa}.autumn .cs{color:#00a}.autumn .gd,.autumn .gr{color:#a00}.autumn .gh{color:navy}.autumn .gi{color:#0a0}.autumn .go{color:#888}.autumn .gp{color:#555}.autumn .gu{color:purple}.autumn .gt{color:#a00}.autumn .kc,.autumn .kd,.autumn .kn,.autumn .kp,.autumn .kr{color:#00a}.autumn .kt{color:#0aa}.autumn .m{color:#099}.autumn .s{color:#a50}.autumn .na{color:#1e90ff}.autumn .nb{color:#0aa}.autumn .nc{color:#0a0}.autumn .no{color:#a00}.autumn .nd{color:#888}.autumn .ni{color:#800}.autumn .nf{color:#0a0}.autumn .nn{color:#0aa}.autumn .nt{color:#1e90ff}.autumn .nv{color:#a00}.autumn .ow{color:#00a}.autumn .w{color:#bbb}.autumn .mb,.autumn .mf,.autumn .mh,.autumn .mi,.autumn .mo{color:#099}.autumn .s2,.autumn .sb,.autumn .sc,.autumn .sd,.autumn .se,.autumn .sh,.autumn .si,.autumn .sx{color:#a50}.autumn .sr{color:#099}.autumn .s1{color:#a50}.autumn .ss{color:#00a}.autumn .bp{color:#0aa}.autumn .vc,.autumn .vg,.autumn .vi{color:#a00}.autumn .il{color:#099}', 'vs': '.vs .hll{background-color:#ffc}.vs{background:#fff}.vs .c{color:green}.vs .err{border:1px solid red}.vs .k{color:#00f}.vs .cm{color:green}.vs .cp{color:#00f}.vs .c1,.vs .cs{color:green}.vs .ge{font-style:italic}.vs .gh,.vs .gp,.vs .gs,.vs .gu{font-weight:700}.vs .kc,.vs .kd,.vs .kn,.vs .kp,.vs .kr{color:#00f}.vs .kt{color:#2b91af}.vs .s{color:#a31515}.vs .nc{color:#2b91af}.vs .ow{color:#00f}.vs .s1,.vs .s2,.vs .sb,.vs .sc,.vs .sd,.vs .se,.vs .sh,.vs .si,.vs .sr,.vs .ss,.vs .sx{color:#a31515}', 'rrt': '.rrt .hll{background-color:#00f}.rrt{background:#000}.rrt .c{color:#0f0}.rrt .k{color:red}.rrt .cm{color:#0f0}.rrt .cp{color:#e5e5e5}.rrt .c1,.rrt .cs{color:#0f0}.rrt .kc,.rrt .kd,.rrt .kn,.rrt .kp,.rrt .kr{color:red}.rrt .kt{color:violet}.rrt .s{color:#87ceeb}.rrt .no{color:#7fffd4}.rrt .nf{color:#ff0}.rrt .nv{color:#eedd82}.rrt .s1,.rrt .s2,.rrt .sb,.rrt .sc,.rrt .sd,.rrt .se,.rrt .sh,.rrt .si,.rrt .sr,.rrt .ss,.rrt .sx{color:#87ceeb}.rrt .vc,.rrt .vg,.rrt .vi{color:#eedd82}', 'native': '.native .c,.native .c1,.native .cm,.native .ge{font-style:italic}.native .gu,.native .nc,.native .nn{text-decoration:underline}.native .cp,.native .cs,.native .gh,.native .gs,.native .k,.native .kr,.native .kt,.native .nt,.native .ow{font-weight:700}.native .hll{background-color:#404040}.native{background:#202020;color:#d0d0d0}.native .c{color:#999}.native .err{color:#a61717;background-color:#e3d2d2}.native .esc,.native .g{color:#d0d0d0}.native .k{color:#6ab825}.native .l,.native .n,.native .o,.native .p,.native .x{color:#d0d0d0}.native .cm{color:#999}.native .cp{color:#cd2828}.native .c1{color:#999}.native .cs{color:#e50808;background-color:#520000}.native .gd{color:#d22323}.native .ge{color:#d0d0d0}.native .gr{color:#d22323}.native .gh{color:#fff}.native .gi{color:#589819}.native .go{color:#ccc}.native .gp{color:#aaa}.native .gs{color:#d0d0d0}.native .gu{color:#fff}.native .gt{color:#d22323}.native .kc,.native .kd,.native .kn{color:#6ab825;font-weight:700}.native .kp,.native .kr,.native .kt{color:#6ab825}.native .ld{color:#d0d0d0}.native .m{color:#3677a9}.native .s{color:#ed9d13}.native .na{color:#bbb}.native .nb{color:#24909d}.native .nc{color:#447fcf}.native .no{color:#40ffff}.native .nd{color:orange}.native .ni{color:#d0d0d0}.native .ne{color:#bbb}.native .nf{color:#447fcf}.native .nl{color:#d0d0d0}.native .nn{color:#447fcf}.native .nx,.native .py{color:#d0d0d0}.native .nt{color:#6ab825}.native .nv{color:#40ffff}.native .ow{color:#6ab825}.native .w{color:#666}.native .mb,.native .mf,.native .mh,.native .mi,.native .mo{color:#3677a9}.native .s2,.native .sb,.native .sc,.native .sd,.native .se,.native .sh,.native .si{color:#ed9d13}.native .sx{color:orange}.native .s1,.native .sr,.native .ss{color:#ed9d13}.native .bp{color:#24909d}.native .vc,.native .vg,.native .vi{color:#40ffff}.native .il{color:#3677a9}', 'perldoc': '.perldoc .ge,.perldoc .sh{font-style:italic}.perldoc .hll{background-color:#ffc}.perldoc{background:#eed}.perldoc .c{color:#228B22}.perldoc .err{color:#a61717;background-color:#e3d2d2}.perldoc .k{color:#8B008B;font-weight:700}.perldoc .cm{color:#228B22}.perldoc .cp{color:#1e889b}.perldoc .c1{color:#228B22}.perldoc .cs{color:#8B008B;font-weight:700}.perldoc .gd,.perldoc .gr{color:#a00}.perldoc .gh{color:navy;font-weight:700}.perldoc .gi{color:#0a0}.perldoc .go{color:#888}.perldoc .gp{color:#555}.perldoc .gs{font-weight:700}.perldoc .gu{color:purple;font-weight:700}.perldoc .gt{color:#a00}.perldoc .kc,.perldoc .kd,.perldoc .kn,.perldoc .kp,.perldoc .kr{color:#8B008B;font-weight:700}.perldoc .kt{color:#a7a7a7;font-weight:700}.perldoc .m{color:#B452CD}.perldoc .s{color:#CD5555}.perldoc .na,.perldoc .nb{color:#658b00}.perldoc .nc{color:#008b45;font-weight:700}.perldoc .no{color:#00688B}.perldoc .nd{color:#707a7c}.perldoc .ne,.perldoc .nf,.perldoc .nn{color:#008b45}.perldoc .ne{font-weight:700}.perldoc .nn{text-decoration:underline}.perldoc .nt{color:#8B008B;font-weight:700}.perldoc .nv{color:#00688B}.perldoc .ow{color:#8B008B}.perldoc .w{color:#bbb}.perldoc .mb,.perldoc .mf,.perldoc .mh,.perldoc .mi,.perldoc .mo{color:#B452CD}.perldoc .s2,.perldoc .sb,.perldoc .sc,.perldoc .sd,.perldoc .se{color:#CD5555}.perldoc .sh{color:#1c7e71}.perldoc .si{color:#CD5555}.perldoc .sx{color:#cb6c20}.perldoc .sr{color:#1c7e71}.perldoc .s1,.perldoc .ss{color:#CD5555}.perldoc .bp{color:#658b00}.perldoc .vc,.perldoc .vg,.perldoc .vi{color:#00688B}.perldoc .il{color:#B452CD}', 'borland': '.borland .c,.borland .c1,.borland .cm,.borland .ge{font-style:italic}.borland .cs,.borland .gs,.borland .k,.borland .nt,.borland .ow{font-weight:700}.borland .hll{background-color:#ffc}.borland{background:#fff}.borland .c{color:#080}.borland .err{color:#a61717;background-color:#e3d2d2}.borland .k{color:navy}.borland .cm{color:#080}.borland .cp{color:teal}.borland .c1,.borland .cs{color:#080}.borland .gd{color:#000;background-color:#fdd}.borland .gr{color:#a00}.borland .gh{color:#999}.borland .gi{color:#000;background-color:#dfd}.borland .go{color:#888}.borland .gp{color:#555}.borland .gu{color:#aaa}.borland .gt{color:#a00}.borland .kc,.borland .kd,.borland .kn,.borland .kp,.borland .kr,.borland .kt{color:navy;font-weight:700}.borland .m,.borland .s{color:#00F}.borland .na{color:red}.borland .nt{color:navy}.borland .w{color:#bbb}.borland .mb,.borland .mf,.borland .mh,.borland .mi,.borland .mo,.borland .sb{color:#00F}.borland .sc{color:purple}.borland .il,.borland .s1,.borland .s2,.borland .sd,.borland .se,.borland .sh,.borland .si,.borland .sr,.borland .ss,.borland .sx{color:#00F}', 'tango': '.tango .c,.tango .ge,.tango .go,.tango .sd{font-style:italic}.tango .gh,.tango .gs,.tango .gt,.tango .gu,.tango .il,.tango .k,.tango .m,.tango .mb,.tango .mf,.tango .mh,.tango .mi,.tango .mo,.tango .nd,.tango .ne,.tango .nt,.tango .o,.tango .ow,.tango .p{font-weight:700}.tango .hll{background-color:#ffc}.tango{background:#f8f8f8}.tango .c{color:#8f5902}.tango .err{color:#a40000;border:1px solid #ef2929}.tango .g{color:#000}.tango .k{color:#204a87}.tango .l,.tango .n{color:#000}.tango .o{color:#ce5c00}.tango .p,.tango .x{color:#000}.tango .c1,.tango .cm,.tango .cp,.tango .cs{color:#8f5902;font-style:italic}.tango .gd{color:#a40000}.tango .ge{color:#000}.tango .gr{color:#ef2929}.tango .gh{color:navy}.tango .gi{color:#00A000}.tango .go{color:#000}.tango .gp{color:#8f5902}.tango .gs{color:#000}.tango .gu{color:purple}.tango .gt{color:#a40000}.tango .kc,.tango .kd,.tango .kn,.tango .kp,.tango .kr,.tango .kt{color:#204a87;font-weight:700}.tango .ld{color:#000}.tango .m{color:#0000cf}.tango .s{color:#4e9a06}.tango .na{color:#c4a000}.tango .nb{color:#204a87}.tango .nc,.tango .no{color:#000}.tango .nd{color:#5c35cc}.tango .ni{color:#ce5c00}.tango .ne{color:#c00}.tango .nf{color:#000}.tango .nl{color:#f57900}.tango .nn,.tango .nx,.tango .py{color:#000}.tango .nt{color:#204a87}.tango .nv{color:#000}.tango .ow{color:#204a87}.tango .w{color:#f8f8f8;text-decoration:underline}.tango .mb,.tango .mf,.tango .mh,.tango .mi,.tango .mo{color:#0000cf}.tango .sb,.tango .sc{color:#4e9a06}.tango .sd{color:#8f5902}.tango .s1,.tango .s2,.tango .se,.tango .sh,.tango .si,.tango .sr,.tango .ss,.tango .sx{color:#4e9a06}.tango .bp{color:#3465a4}.tango .vc,.tango .vg,.tango .vi{color:#000}.tango .il{color:#0000cf}', 'emacs': '.emacs .c,.emacs .c1,.emacs .cm,.emacs .ge,.emacs .sd{font-style:italic}.emacs .cs,.emacs .gh,.emacs .gp,.emacs .gs,.emacs .gu,.emacs .k,.emacs .kc,.emacs .kd,.emacs .kn,.emacs .kt,.emacs .ne,.emacs .ni,.emacs .nn,.emacs .nt,.emacs .ow,.emacs .se,.emacs .si{font-weight:700}.emacs .hll{background-color:#ffc}.emacs{background:#f8f8f8}.emacs .c{color:#080}.emacs .err{border:1px solid red}.emacs .k{color:#A2F}.emacs .o{color:#666}.emacs .c1,.emacs .cm,.emacs .cp,.emacs .cs{color:#080}.emacs .gd{color:#A00000}.emacs .gr{color:red}.emacs .gh{color:navy}.emacs .gi{color:#00A000}.emacs .go{color:#888}.emacs .gp{color:navy}.emacs .gu{color:purple}.emacs .gt{color:#04D}.emacs .kc,.emacs .kd,.emacs .kn,.emacs .kp,.emacs .kr{color:#A2F}.emacs .kr{font-weight:700}.emacs .kt{color:#0B0}.emacs .m{color:#666}.emacs .na,.emacs .s{color:#B44}.emacs .nb{color:#A2F}.emacs .nc{color:#00F}.emacs .no{color:#800}.emacs .nd{color:#A2F}.emacs .ni{color:#999}.emacs .ne{color:#D2413A}.emacs .nf{color:#00A000}.emacs .nl{color:#A0A000}.emacs .nn{color:#00F}.emacs .nt{color:green}.emacs .nv{color:#B8860B}.emacs .ow{color:#A2F}.emacs .w{color:#bbb}.emacs .mb,.emacs .mf,.emacs .mh,.emacs .mi,.emacs .mo{color:#666}.emacs .s2,.emacs .sb,.emacs .sc,.emacs .sd{color:#B44}.emacs .se{color:#B62}.emacs .sh{color:#B44}.emacs .si{color:#B68}.emacs .sx{color:green}.emacs .sr{color:#B68}.emacs .s1{color:#B44}.emacs .ss{color:#B8860B}.emacs .bp{color:#A2F}.emacs .vc,.emacs .vg,.emacs .vi{color:#B8860B}.emacs .il{color:#666}', 'friendly': '.friendly .gh,.friendly .gp,.friendly .gs,.friendly .gu,.friendly .k,.friendly .kc,.friendly .kd,.friendly .kn,.friendly .kr,.friendly .nd,.friendly .ni,.friendly .nl,.friendly .nn,.friendly .nt,.friendly .ow,.friendly .se{font-weight:700}.friendly .c,.friendly .c1,.friendly .cm,.friendly .ge,.friendly .sd,.friendly .si{font-style:italic}.friendly .hll{background-color:#ffc}.friendly{background:#f0f0f0}.friendly .c{color:#60a0b0}.friendly .err{border:1px solid red}.friendly .k{color:#007020}.friendly .o{color:#666}.friendly .cm{color:#60a0b0}.friendly .cp{color:#007020}.friendly .c1{color:#60a0b0}.friendly .cs{color:#60a0b0;background-color:#fff0f0}.friendly .gd{color:#A00000}.friendly .gr{color:red}.friendly .gh{color:navy}.friendly .gi{color:#00A000}.friendly .go{color:#888}.friendly .gp{color:#c65d09}.friendly .gu{color:purple}.friendly .gt{color:#04D}.friendly .kc,.friendly .kd,.friendly .kn,.friendly .kp,.friendly .kr{color:#007020}.friendly .kt{color:#902000}.friendly .m{color:#40a070}.friendly .na,.friendly .s{color:#4070a0}.friendly .nb{color:#007020}.friendly .nc{color:#0e84b5;font-weight:700}.friendly .no{color:#60add5}.friendly .nd{color:#555}.friendly .ni{color:#d55537}.friendly .ne{color:#007020}.friendly .nf{color:#06287e}.friendly .nl{color:#002070}.friendly .nn{color:#0e84b5}.friendly .nt{color:#062873}.friendly .nv{color:#bb60d5}.friendly .ow{color:#007020}.friendly .w{color:#bbb}.friendly .mb,.friendly .mf,.friendly .mh,.friendly .mi,.friendly .mo{color:#40a070}.friendly .s2,.friendly .sb,.friendly .sc,.friendly .sd,.friendly .se,.friendly .sh{color:#4070a0}.friendly .si{color:#70a0d0}.friendly .sx{color:#c65d09}.friendly .sr{color:#235388}.friendly .s1{color:#4070a0}.friendly .ss{color:#517918}.friendly .bp{color:#007020}.friendly .vc,.friendly .vg,.friendly .vi{color:#bb60d5}.friendly .il{color:#40a070}', 'monokai': '.monokai .hll{background-color:#49483e}.monokai{background:#272822;color:#f8f8f2}.monokai .c{color:#75715e}.monokai .err{color:#960050;background-color:#1e0010}.monokai .k{color:#66d9ef}.monokai .l{color:#ae81ff}.monokai .n{color:#f8f8f2}.monokai .o{color:#f92672}.monokai .p{color:#f8f8f2}.monokai .c1,.monokai .cm,.monokai .cp,.monokai .cs{color:#75715e}.monokai .gd{color:#f92672}.monokai .ge{font-style:italic}.monokai .gi{color:#a6e22e}.monokai .gs{font-weight:700}.monokai .gu{color:#75715e}.monokai .kc,.monokai .kd{color:#66d9ef}.monokai .kn{color:#f92672}.monokai .kp,.monokai .kr,.monokai .kt{color:#66d9ef}.monokai .ld{color:#e6db74}.monokai .m{color:#ae81ff}.monokai .s{color:#e6db74}.monokai .na{color:#a6e22e}.monokai .nb{color:#f8f8f2}.monokai .nc{color:#a6e22e}.monokai .no{color:#66d9ef}.monokai .nd{color:#a6e22e}.monokai .ni{color:#f8f8f2}.monokai .ne,.monokai .nf{color:#a6e22e}.monokai .nl,.monokai .nn{color:#f8f8f2}.monokai .nx{color:#a6e22e}.monokai .py{color:#f8f8f2}.monokai .nt{color:#f92672}.monokai .nv{color:#f8f8f2}.monokai .ow{color:#f92672}.monokai .w{color:#f8f8f2}.monokai .mb,.monokai .mf,.monokai .mh,.monokai .mi,.monokai .mo{color:#ae81ff}.monokai .s2,.monokai .sb,.monokai .sc,.monokai .sd{color:#e6db74}.monokai .se{color:#ae81ff}.monokai .s1,.monokai .sh,.monokai .si,.monokai .sr,.monokai .ss,.monokai .sx{color:#e6db74}.monokai .bp,.monokai .vc,.monokai .vg,.monokai .vi{color:#f8f8f2}.monokai .il{color:#ae81ff}', 'paraiso-dark': '.paraiso-dark .hll{background-color:#4f424c}.paraiso-dark{background:#2f1e2e;color:#e7e9db}.paraiso-dark .c{color:#776e71}.paraiso-dark .err{color:#ef6155}.paraiso-dark .k{color:#815ba4}.paraiso-dark .l{color:#f99b15}.paraiso-dark .n{color:#e7e9db}.paraiso-dark .o{color:#5bc4bf}.paraiso-dark .p{color:#e7e9db}.paraiso-dark .c1,.paraiso-dark .cm,.paraiso-dark .cp,.paraiso-dark .cs{color:#776e71}.paraiso-dark .gd{color:#ef6155}.paraiso-dark .ge{font-style:italic}.paraiso-dark .gh{color:#e7e9db;font-weight:700}.paraiso-dark .gi{color:#48b685}.paraiso-dark .gp{color:#776e71;font-weight:700}.paraiso-dark .gs{font-weight:700}.paraiso-dark .gu{color:#5bc4bf;font-weight:700}.paraiso-dark .kc,.paraiso-dark .kd{color:#815ba4}.paraiso-dark .kn{color:#5bc4bf}.paraiso-dark .kp,.paraiso-dark .kr{color:#815ba4}.paraiso-dark .kt{color:#fec418}.paraiso-dark .ld{color:#48b685}.paraiso-dark .m{color:#f99b15}.paraiso-dark .s{color:#48b685}.paraiso-dark .na{color:#06b6ef}.paraiso-dark .nb{color:#e7e9db}.paraiso-dark .nc{color:#fec418}.paraiso-dark .no{color:#ef6155}.paraiso-dark .nd{color:#5bc4bf}.paraiso-dark .ni{color:#e7e9db}.paraiso-dark .ne{color:#ef6155}.paraiso-dark .nf{color:#06b6ef}.paraiso-dark .nl{color:#e7e9db}.paraiso-dark .nn{color:#fec418}.paraiso-dark .nx{color:#06b6ef}.paraiso-dark .py{color:#e7e9db}.paraiso-dark .nt{color:#5bc4bf}.paraiso-dark .nv{color:#ef6155}.paraiso-dark .ow{color:#5bc4bf}.paraiso-dark .w{color:#e7e9db}.paraiso-dark .mb,.paraiso-dark .mf,.paraiso-dark .mh,.paraiso-dark .mi,.paraiso-dark .mo{color:#f99b15}.paraiso-dark .sb{color:#48b685}.paraiso-dark .sc{color:#e7e9db}.paraiso-dark .sd{color:#776e71}.paraiso-dark .s2{color:#48b685}.paraiso-dark .se{color:#f99b15}.paraiso-dark .sh{color:#48b685}.paraiso-dark .si{color:#f99b15}.paraiso-dark .s1,.paraiso-dark .sr,.paraiso-dark .ss,.paraiso-dark .sx{color:#48b685}.paraiso-dark .bp{color:#e7e9db}.paraiso-dark .vc,.paraiso-dark .vg,.paraiso-dark .vi{color:#ef6155}.paraiso-dark .il{color:#f99b15}', 'colorful': '.colorful .cs,.colorful .gh,.colorful .gp,.colorful .gs,.colorful .gu,.colorful .il,.colorful .k,.colorful .kc,.colorful .kd,.colorful .kn,.colorful .kp,.colorful .kr,.colorful .kt,.colorful .m,.colorful .mb,.colorful .mf,.colorful .mh,.colorful .mi,.colorful .mo,.colorful .nc,.colorful .ne,.colorful .nf,.colorful .ni,.colorful .nl,.colorful .nn,.colorful .no,.colorful .ow,.colorful .se,.colorful .vg{font-weight:700}.colorful .hll{background-color:#ffc}.colorful{background:#fff}.colorful .c{color:#888}.colorful .err{color:red;background-color:#FAA}.colorful .s,.colorful .s2,.colorful .sb,.colorful .se,.colorful .sh{background-color:#fff0f0}.colorful .k{color:#080}.colorful .o{color:#333}.colorful .cm{color:#888}.colorful .cp{color:#579}.colorful .c1{color:#888}.colorful .cs{color:#c00}.colorful .gd{color:#A00000}.colorful .ge{font-style:italic}.colorful .gr{color:red}.colorful .gh{color:navy}.colorful .gi{color:#00A000}.colorful .go{color:#888}.colorful .gp{color:#c65d09}.colorful .gu{color:purple}.colorful .gt{color:#04D}.colorful .kc,.colorful .kd,.colorful .kn{color:#080}.colorful .kp{color:#038}.colorful .kr{color:#080}.colorful .kt{color:#339}.colorful .m{color:#60E}.colorful .na{color:#00C}.colorful .nb{color:#007020}.colorful .nc{color:#B06}.colorful .no{color:#036}.colorful .nd{color:#555;font-weight:700}.colorful .ni{color:#800}.colorful .ne{color:red}.colorful .nf{color:#06B}.colorful .nl{color:#970}.colorful .nn{color:#0e84b5}.colorful .nt{color:#070}.colorful .nv{color:#963}.colorful .ow{color:#000}.colorful .w{color:#bbb}.colorful .mb,.colorful .mf{color:#60E}.colorful .mh{color:#058}.colorful .mi{color:#00D}.colorful .mo{color:#40E}.colorful .sc{color:#04D}.colorful .sd{color:#D42}.colorful .se{color:#666}.colorful .si{background-color:#eee}.colorful .sx{color:#D20;background-color:#fff0f0}.colorful .sr{color:#000;background-color:#fff0ff}.colorful .s1{background-color:#fff0f0}.colorful .ss{color:#A60}.colorful .bp{color:#007020}.colorful .vc{color:#369}.colorful .vg{color:#d70}.colorful .vi{color:#33B}.colorful .il{color:#00D}', 'murphy': '.murphy .c,.murphy .c1,.murphy .cm,.murphy .cs,.murphy .ge{font-style:italic}.murphy .cs,.murphy .gh,.murphy .gp,.murphy .gs,.murphy .gu,.murphy .il,.murphy .k,.murphy .kc,.murphy .kd,.murphy .kn,.murphy .kp,.murphy .kr,.murphy .kt,.murphy .m,.murphy .mb,.murphy .mf,.murphy .mh,.murphy .mi,.murphy .mo,.murphy .nc,.murphy .nd,.murphy .ne,.murphy .nf,.murphy .nl,.murphy .nn,.murphy .ow,.murphy .se{font-weight:700}.murphy .hll{background-color:#ffc}.murphy{background:#fff}.murphy .c{color:#666}.murphy .err{color:red;background-color:#FAA}.murphy .s,.murphy .s2,.murphy .sb,.murphy .se,.murphy .sh{background-color:#e0e0ff}.murphy .k{color:#289}.murphy .o{color:#333}.murphy .cm{color:#666}.murphy .cp{color:#579}.murphy .c1{color:#666}.murphy .cs{color:#c00}.murphy .gd{color:#A00000}.murphy .gr{color:red}.murphy .gh{color:navy}.murphy .gi{color:#00A000}.murphy .go{color:#888}.murphy .gp{color:#c65d09}.murphy .gu{color:purple}.murphy .gt{color:#04D}.murphy .kc,.murphy .kd,.murphy .kn{color:#289}.murphy .kp{color:#08f}.murphy .kr{color:#289}.murphy .kt{color:#66f}.murphy .m{color:#60E}.murphy .na{color:#007}.murphy .nb{color:#072}.murphy .nc{color:#e9e}.murphy .no{color:#5ed;font-weight:700}.murphy .nd{color:#555}.murphy .ni{color:#800}.murphy .ne{color:red}.murphy .nf{color:#5ed}.murphy .nl{color:#970}.murphy .nn{color:#0e84b5}.murphy .nt{color:#070}.murphy .nv{color:#036}.murphy .ow{color:#000}.murphy .w{color:#bbb}.murphy .mb,.murphy .mf{color:#60E}.murphy .mh{color:#058}.murphy .mi{color:#66f}.murphy .mo{color:#40E}.murphy .sc{color:#88F}.murphy .sd{color:#D42}.murphy .se{color:#666}.murphy .si{background-color:#eee}.murphy .s1,.murphy .sr,.murphy .sx{background-color:#e0e0ff}.murphy .sx{color:#f88}.murphy .sr{color:#000}.murphy .ss{color:#fc8}.murphy .bp{color:#072}.murphy .vc{color:#ccf}.murphy .vg{color:#f84}.murphy .vi{color:#aaf}.murphy .il{color:#66f}', 'bw': '.bw .gh,.bw .gp,.bw .gs,.bw .gu,.bw .k,.bw .kc,.bw .kd,.bw .kn,.bw .kr,.bw .nc,.bw .ne,.bw .ni,.bw .nn,.bw .nt,.bw .ow,.bw .se,.bw .si{font-weight:700}.bw .c,.bw .c1,.bw .cm,.bw .cs,.bw .ge,.bw .s,.bw .s1,.bw .s2,.bw .sb,.bw .sc,.bw .sd,.bw .se,.bw .sh,.bw .si,.bw .sr,.bw .ss,.bw .sx{font-style:italic}.bw .hll{background-color:#ffc}.bw{background:#fff}.bw .err{border:1px solid red}', 'pastie': '.pastie .ge,.pastie .nl{font-style:italic}.pastie .hll{background-color:#ffc}.pastie{background:#fff}.pastie .c{color:#888}.pastie .err{color:#a61717;background-color:#e3d2d2}.pastie .k{color:#080;font-weight:700}.pastie .cm{color:#888}.pastie .cp{color:#c00;font-weight:700}.pastie .c1{color:#888}.pastie .cs{color:#c00;font-weight:700;background-color:#fff0f0}.pastie .gd{color:#000;background-color:#fdd}.pastie .gr{color:#a00}.pastie .gh{color:#333}.pastie .gi{color:#000;background-color:#dfd}.pastie .s,.pastie .se,.pastie .sh,.pastie .si{background-color:#fff0f0}.pastie .go{color:#888}.pastie .gp{color:#555}.pastie .gs{font-weight:700}.pastie .gu{color:#666}.pastie .gt{color:#a00}.pastie .kc,.pastie .kd,.pastie .kn{color:#080;font-weight:700}.pastie .kp{color:#080}.pastie .kr{color:#080;font-weight:700}.pastie .kt{color:#888;font-weight:700}.pastie .m{color:#00D;font-weight:700}.pastie .s{color:#d20}.pastie .na{color:#369}.pastie .nb{color:#038}.pastie .nc{color:#b06;font-weight:700}.pastie .no{color:#036;font-weight:700}.pastie .nd{color:#555}.pastie .ne{color:#b06;font-weight:700}.pastie .nf{color:#06b;font-weight:700}.pastie .nl{color:#369}.pastie .nn{color:#b06;font-weight:700}.pastie .py{color:#369;font-weight:700}.pastie .nt{color:#b06;font-weight:700}.pastie .nv{color:#369}.pastie .ow{color:#080}.pastie .w{color:#bbb}.pastie .mb,.pastie .mf,.pastie .mh,.pastie .mi,.pastie .mo{color:#00D;font-weight:700}.pastie .s2,.pastie .sb,.pastie .sc,.pastie .sd{color:#d20;background-color:#fff0f0}.pastie .se{color:#04d}.pastie .sh{color:#d20}.pastie .si{color:#33b}.pastie .sx{color:#2b2;background-color:#f0fff0}.pastie .sr{color:#080;background-color:#fff0ff}.pastie .s1,.pastie .ss{background-color:#fff0f0}.pastie .s1{color:#d20}.pastie .ss{color:#a60}.pastie .bp{color:#038}.pastie .vc{color:#369}.pastie .vg{color:#d70}.pastie .vi{color:#33b}.pastie .il{color:#00D;font-weight:700}', 'paraiso-light': '.paraiso-light .hll{background-color:#a39e9b}.paraiso-light{background:#e7e9db;color:#2f1e2e}.paraiso-light .c{color:#8d8687}.paraiso-light .err{color:#ef6155}.paraiso-light .k{color:#815ba4}.paraiso-light .l{color:#f99b15}.paraiso-light .n{color:#2f1e2e}.paraiso-light .o{color:#5bc4bf}.paraiso-light .p{color:#2f1e2e}.paraiso-light .c1,.paraiso-light .cm,.paraiso-light .cp,.paraiso-light .cs{color:#8d8687}.paraiso-light .gd{color:#ef6155}.paraiso-light .ge{font-style:italic}.paraiso-light .gh{color:#2f1e2e;font-weight:700}.paraiso-light .gi{color:#48b685}.paraiso-light .gp{color:#8d8687;font-weight:700}.paraiso-light .gs{font-weight:700}.paraiso-light .gu{color:#5bc4bf;font-weight:700}.paraiso-light .kc,.paraiso-light .kd{color:#815ba4}.paraiso-light .kn{color:#5bc4bf}.paraiso-light .kp,.paraiso-light .kr{color:#815ba4}.paraiso-light .kt{color:#fec418}.paraiso-light .ld{color:#48b685}.paraiso-light .m{color:#f99b15}.paraiso-light .s{color:#48b685}.paraiso-light .na{color:#06b6ef}.paraiso-light .nb{color:#2f1e2e}.paraiso-light .nc{color:#fec418}.paraiso-light .no{color:#ef6155}.paraiso-light .nd{color:#5bc4bf}.paraiso-light .ni{color:#2f1e2e}.paraiso-light .ne{color:#ef6155}.paraiso-light .nf{color:#06b6ef}.paraiso-light .nl{color:#2f1e2e}.paraiso-light .nn{color:#fec418}.paraiso-light .nx{color:#06b6ef}.paraiso-light .py{color:#2f1e2e}.paraiso-light .nt{color:#5bc4bf}.paraiso-light .nv{color:#ef6155}.paraiso-light .ow{color:#5bc4bf}.paraiso-light .w{color:#2f1e2e}.paraiso-light .mb,.paraiso-light .mf,.paraiso-light .mh,.paraiso-light .mi,.paraiso-light .mo{color:#f99b15}.paraiso-light .sb{color:#48b685}.paraiso-light .sc{color:#2f1e2e}.paraiso-light .sd{color:#8d8687}.paraiso-light .s2{color:#48b685}.paraiso-light .se{color:#f99b15}.paraiso-light .sh{color:#48b685}.paraiso-light .si{color:#f99b15}.paraiso-light .s1,.paraiso-light .sr,.paraiso-light .ss,.paraiso-light .sx{color:#48b685}.paraiso-light .bp{color:#2f1e2e}.paraiso-light .vc,.paraiso-light .vg,.paraiso-light .vi{color:#ef6155}.paraiso-light .il{color:#f99b15}', 'trac': '.trac .c,.trac .c1,.trac .cm,.trac .cs,.trac .ge{font-style:italic}.trac .cp,.trac .cs,.trac .gs,.trac .k,.trac .kc,.trac .kd,.trac .kn,.trac .kp,.trac .kr,.trac .kt,.trac .nc,.trac .o,.trac .ow{font-weight:700}.trac .hll{background-color:#ffc}.trac{background:#fff}.trac .c{color:#998}.trac .err{color:#a61717;background-color:#e3d2d2}.trac .cm{color:#998}.trac .cp{color:#999}.trac .c1{color:#998}.trac .cs{color:#999}.trac .gd{color:#000;background-color:#fdd}.trac .gr{color:#a00}.trac .gh{color:#999}.trac .gi{color:#000;background-color:#dfd}.trac .go{color:#888}.trac .gp{color:#555}.trac .gu{color:#aaa}.trac .gt{color:#a00}.trac .kt{color:#458}.trac .m{color:#099}.trac .s{color:#b84}.trac .na{color:teal}.trac .nb{color:#999}.trac .nc{color:#458}.trac .no{color:teal}.trac .ni{color:purple}.trac .ne,.trac .nf{color:#900;font-weight:700}.trac .nn{color:#555}.trac .nt{color:navy}.trac .nv{color:teal}.trac .w{color:#bbb}.trac .mb,.trac .mf,.trac .mh,.trac .mi,.trac .mo{color:#099}.trac .s2,.trac .sb,.trac .sc,.trac .sd,.trac .se,.trac .sh,.trac .si,.trac .sx{color:#b84}.trac .sr{color:olive}.trac .s1,.trac .ss{color:#b84}.trac .bp{color:#999}.trac .vc,.trac .vg,.trac .vi{color:teal}.trac .il{color:#099}', 'default': '.default .c,.default .cm,.default .ge,.default .sd{font-style:italic}.default .gh,.default .gp,.default .gs,.default .gu,.default .k,.default .kc,.default .kd,.default .kn,.default .kr,.default .ne,.default .ni,.default .nn,.default .nt,.default .ow,.default .se,.default .si{font-weight:700}.default .hll{background-color:#ffc}.default{background:#f8f8f8}.default .c{color:#408080}.default .err{border:1px solid red}.default .k{color:green}.default .o{color:#666}.default .cm{color:#408080}.default .cp{color:#BC7A00}.default .c1,.default .cs{color:#408080;font-style:italic}.default .gd{color:#A00000}.default .gr{color:red}.default .gh{color:navy}.default .gi{color:#00A000}.default .go{color:#888}.default .gp{color:navy}.default .gu{color:purple}.default .gt{color:#04D}.default .kc,.default .kd,.default .kn{color:green}.default .kp,.default .kr{color:green}.default .kt{color:#B00040}.default .m{color:#666}.default .s{color:#BA2121}.default .na{color:#7D9029}.default .nb{color:green}.default .nc{color:#00F;font-weight:700}.default .no{color:#800}.default .nd{color:#A2F}.default .ni{color:#999}.default .ne{color:#D2413A}.default .nf{color:#00F}.default .nl{color:#A0A000}.default .nn{color:#00F}.default .nt{color:green}.default .nv{color:#19177C}.default .ow{color:#A2F}.default .w{color:#bbb}.default .mb,.default .mf,.default .mh,.default .mi,.default .mo{color:#666}.default .s2,.default .sb,.default .sc,.default .sd{color:#BA2121}.default .se{color:#B62}.default .sh{color:#BA2121}.default .si{color:#B68}.default .sx{color:green}.default .sr{color:#B68}.default .s1{color:#BA2121}.default .ss{color:#19177C}.default .bp{color:green}.default .vc,.default .vg,.default .vi{color:#19177C}.default .il{color:#666}', 'fruity': '.fruity .hll{background-color:#333}.fruity{background:#111;color:#fff}.fruity .c,.fruity .c1,.fruity .cm,.fruity .cp,.fruity .cs{font-style:italic;background-color:#0f140f}.fruity .c{color:#080}.fruity .err,.fruity .esc,.fruity .g{color:#fff}.fruity .k{color:#fb660a;font-weight:700}.fruity .l,.fruity .n,.fruity .o,.fruity .p,.fruity .x{color:#fff}.fruity .cm{color:#080}.fruity .cp{color:#ff0007;font-weight:700}.fruity .c1,.fruity .cs{color:#080}.fruity .gd,.fruity .ge,.fruity .gi,.fruity .gr{color:#fff}.fruity .gh{color:#fff;font-weight:700}.fruity .go{color:#444;background-color:#222}.fruity .gp,.fruity .gs,.fruity .gt{color:#fff}.fruity .gu{color:#fff;font-weight:700}.fruity .kp,.fruity .kr{color:#fb660a}.fruity .kc,.fruity .kd,.fruity .kn{color:#fb660a;font-weight:700}.fruity .kr{font-weight:700}.fruity .kt{color:#cdcaa9;font-weight:700}.fruity .ld{color:#fff}.fruity .m{color:#0086f7;font-weight:700}.fruity .s{color:#0086d2}.fruity .na{color:#ff0086;font-weight:700}.fruity .nb,.fruity .nc{color:#fff}.fruity .no{color:#0086d2}.fruity .nd,.fruity .ne,.fruity .ni{color:#fff}.fruity .nf{color:#ff0086;font-weight:700}.fruity .nl,.fruity .nn,.fruity .nx,.fruity .py{color:#fff}.fruity .nt,.fruity .nv{color:#fb660a}.fruity .nt{font-weight:700}.fruity .ow{color:#fff}.fruity .w{color:#888}.fruity .mb,.fruity .mf,.fruity .mh,.fruity .mi,.fruity .mo{color:#0086f7;font-weight:700}.fruity .s1,.fruity .s2,.fruity .sb,.fruity .sc,.fruity .sd,.fruity .se,.fruity .sh,.fruity .si,.fruity .sr,.fruity .ss,.fruity .sx{color:#0086d2}.fruity .bp{color:#fff}.fruity .vc,.fruity .vg,.fruity .vi{color:#fb660a}.fruity .il{color:#0086f7;font-weight:700}'}
	text = '<style>'+style_css[style]+'</style><span style="font-size:'+font_size+'px;">'+code_highlighted+'</span>'
	return render_template('index.html',preview=Markup(text),code=code)

if __name__ == '__main__':
	app.run(debug=True)