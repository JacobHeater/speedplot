from scss.compiler import Compiler

src_file_path = './scss/index.scss'
out_file_path = './static/styles/speedplot.css'

print 'Compiling ./scss/index.scss'

output = Compiler().compile(src_file_path)

print 'Compilation complete!'
print 'Writing output to %s...' % out_file_path

with open(out_file_path, 'w') as out_file:
    out_file.write(output)

    print 'Output has been written to %s!' % out_file_path

print 'Done!'