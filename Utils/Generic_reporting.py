from datetime import datetime

def write_the_report_header (report_file_stream, page_title):
    # writes the header of the report file

    # open the report file stream

    report_header_file_name = "Input\\report_header.input"
    report_header_file_stream = open(report_header_file_name, mode='r')

    report_file_stream.write("<!DOCTYPE html>")
    report_file_stream.write("<html xmlns='http://www.w3.org/1999/xhtml'>")

    # copy all the header lines form a data file to the report file
    for line in report_header_file_stream:
        report_file_stream.write(line)

    report_file_stream.write("<body>")
    report_file_stream.write("<h1 class='title'>%s</h1>" % page_title)
    report_file_stream.write("<h2 class='date-header'>%s</h2>" % datetime.now().strftime("%d/%m/%Y  %H:%M:%S"))
    report_file_stream.write("<h3 class='post-title'>")
    report_file_stream.write("<a href=''>Test Steps (Web Page Interaction)</a>")
    report_file_stream.write("</h3>")
    report_file_stream.write("<div class='post-body'>")