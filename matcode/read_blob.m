
function [data] = read_blob(fn)

f = fopen(fn, 'r');

m = 512;

% data is the blob binary data in single precision (e.g float in C++)
data = fread(f, [1 m], 'single');
fclose(f);

end