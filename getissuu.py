#!/usr/bin/env python3
import itertools, os, subprocess, sys
from argparse import ArgumentParser

def main():
	description = ("Downloads a document from issuu.com"
		" and converts it to a high quality PDF file")
	argparser = ArgumentParser(description=description)
	argparser.add_argument("--curl", action="store", type=str,
		default="/usr/bin/curl", metavar="PATH",
		help="path to curl (default: %(default)s)")
	argparser.add_argument("--swfrender", action="store", type=str,
		default="/usr/bin/swfrender", metavar="PATH",
		help="path to swfrender (default: %(default)s)")
	argparser.add_argument("--convert", action="store", type=str,
		default="/usr/bin/convert", metavar="PATH",
		help="path to convert (default: %(default)s)")
	argparser.add_argument("--document-name", action="store", type=str,
		metavar="NAME", help="name of the document")
	argparser.add_argument("--document-id", action="store", type=str,
		metavar="ID", help="issuu.com document id")
	argparser.add_argument("--dpi", action="store", type=int, default=300,
		help="output DPI (default: %(default)s)")
	argparser.add_argument("--output", action="store", type=str,
		help="output path (default: current directory)")
	options = argparser.parse_args()

	if options.document_name == None:
		options.document_name = input("Name of the document: ")

	if options.document_id == None:
		options.document_id = input("ISSUU document ID: ")

	if options.output == None:
		options.output = os.path.curdir

	name_format = "page_{0:0>3}"
	swf_file = "{0}.swf".format(name_format)
	png_file = "{0}.png".format(name_format)
	swf_path = os.path.join(options.output, options.document_name, "swf")
	png_path = os.path.join(options.output, options.document_name, "png")

	issuu_url = "http://page.issuu.com/{0}/swf/page_{1}.swf"
	page_count = 0

	os.makedirs(swf_path, exist_ok = True)
	print(os.linesep, "Downloading document's pages...", sep="")
	for i in itertools.count(1):
		proc = subprocess.Popen([
			options.curl, "-f", "-s", "-o",
			os.path.join(swf_path, swf_file.format(i)),
			issuu_url.format(options.document_id, i)
		])
		proc.wait()

		if proc.returncode != 0:
			break
		else:
			page_count += 1

		print_pagenum(i)

	os.makedirs(png_path, exist_ok = True)
	print(os.linesep, os.linesep, "Converting pages to images...", sep="")
	for i in range(1, page_count+1):
		subprocess.call([
			options.swfrender,
			os.path.join(swf_path, swf_file.format(i)),
			"-r", str(options.dpi),
			"-o", os.path.join(png_path, png_file.format(i))
		])

		print_pagenum(i)

	print(os.linesep, os.linesep, "Creating a PDF from images...", sep="")
	subprocess.call([
		options.convert, os.path.join(png_path, "*"),
		"-compress", "jpeg", "-density", str(options.dpi),
		os.path.join(options.output, "{0}.pdf".format(options.document_name))
	])

def print_pagenum(num):
	if num > 1:
		print(",", num, end="", flush=True)
	else:
		print(num, end="", flush=True)

if __name__ == "__main__":
	try:
		sys.exit(main())
	except KeyboardInterrupt:
		sys.exit(1)
