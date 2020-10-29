import subprocess
from pdflatex import PDFLaTeX

tex="sample.tex"
pdf="sample.pdf"
svg="sample.svg"
png="sample.png"
aux="sample.aux"
log="sample.log"

def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        pdfl = PDFLaTeX.from_texfile(tex)
        pdf_out, log, completed_process = pdfl.create_pdf(keep_pdf_file=True, keep_log_file=False)
        pdf_crop = crop(["-o", "crop.pdf", "-p4", "0.5", "0", "0.5", "0", "-u", "-s", pdf]) #l,b,r,t
        png = convert_from_path('./crop.pdf', 
            single_file=True,
            dpi=300,
            output_folder='./',
            transparent=True,
            fmt='png',
            output_file=str('output')) 
        clean = subprocess.run(["rm", "-rf", pdf, svg, log, aux])
        print("The exit code was: %d" % clean.returncode)

        
        return f'Hello World!'

