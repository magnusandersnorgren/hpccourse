import hello_ext
import vcf

# test = hello_ext.variants();

# test.add_position(1);
# test.add_position(2);
# test.add_position(3);
# test.add_position(4);
# test.add_position(5);

# test.add_position(10);
# test.add_position(12);
# test.add_position(14);
# test.add_position(16);
# test.add_position(18);
# test.add_position(20);

# test.add_position(100);
# test.add_position(150);
# test.add_position(200);
# test.add_position(250);
# test.add_position(300);

# test.print_container();
# print "stretch 1 " + str(test.maximum_stretch(1));
# print "stretch 2 " + str(test.maximum_stretch(2));
# print "stretch 5 " + str(test.maximum_stretch(5));
# print "stretch 10 " + str(test.maximum_stretch(10));
# print "stretch 20 " + str(test.maximum_stretch(20));
# print "stretch 50 " + str(test.maximum_stretch(50));
# print "stretch 100 " + str(test.maximum_stretch(100));

iCounter = hello_ext.variants();
vcf_reader = vcf.Reader(open('test.vcf.gz', 'r'))

for record in vcf_reader:
    iCounter.add_position(record.POS)

print  "1" + str(iCounter.maximum_stretch(1))
print  "2" + str(iCounter.maximum_stretch(2))
print  "5" + str(iCounter.maximum_stretch(5))
print  "7" + str(iCounter.maximum_stretch(7))
print  "10" + str(iCounter.maximum_stretch(10))
print  "42" + str(iCounter.maximum_stretch(42))
print  "50" + str(iCounter.maximum_stretch(50))
print  "100" + str(iCounter.maximum_stretch(100))
print  "500" + str(iCounter.maximum_stretch(500))
print  "1k" + str(iCounter.maximum_stretch(1000))
print  "5k" + str(iCounter.maximum_stretch(5000))
print  "10k" + str(iCounter.maximum_stretch(10000))
print  "15k" + str(iCounter.maximum_stretch(15000))
print  "20k" + str(iCounter.maximum_stretch(20000))
print  "50k" + str(iCounter.maximum_stretch(50000))
print  "100k" + str(iCounter.maximum_stretch(100000))
print  "1M" + str(iCounter.maximum_stretch(1000000))
