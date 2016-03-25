import unittest
import abcss

class FormatTest(unittest.TestCase):
	def testPadding(self):		
		self.failUnless(abcss.format('banana', 0) == 'banana\n')
		self.failUnless(abcss.format('banana', 1) == '\tbanana\n')
		self.failUnless(abcss.format('banana', 3) == '\t\t\tbanana\n')


class SortTest(unittest.TestCase):
	def testSort(self):
		lines = [
			'display: block;',
			'position: absolute;',
			'float: left;'
		]

		expected = [
			'display: block;',
			'float: left;',
			'position: absolute;'
		]
		
		self.failUnless(abcss.sort(lines) == expected)

	def testHandleVendorPrefixes(self):
		lines = [
			'-webkit-touch-action: none;',
  			'-ms-touch-action: none;',
  			'touch-action: none;',
  			'float: left;'
		]

		expected = [
			'float: left;',
			'-webkit-touch-action: none;',
  			'-ms-touch-action: none;',
  			'touch-action: none;',  			
		]

		self.failUnless(abcss.sort(lines) == expected)

class ParseLinesTest(unittest.TestCase):

	def testEmptyBlock(self):
		lines = [
			'.class-name {\n',
			'}'
		]
		
		self.failUnless(abcss.parse_lines(lines) == lines)

	def testMultipleBlocks(self):
		lines = [
			'.class-name {\n',
			'\t.another-class-name {\n',
			'\t}'
			'}'
		]

		self.failUnless(abcss.parse_lines(lines) == lines)

	def testSingleRule(self):
		lines = [
			'.class-name {\n',
			'\tfloat: left;\n',
			'}'
		]

		self.failUnless(abcss.parse_lines(lines) == lines)

	def testMultipleRulesShouldBeSorted(self):
		lines = [
			'.class-name {\n',
			'\tposition: absolute;',
			'\tfloat: left;',
			'}'
		]		

		expected = [
			'.class-name {\n',			
			'\tfloat: left;',
			'\tposition: absolute;',
			'}'
		]		

	def testNestedBlocks(self):
		lines = [
			'.class-name {\n',
			'\tposition: absolute;',
			'\tfloat: left;',
			'\t.another-class-name {\n',
			'\t\tposition: absolute',
			'\t\tbackground: white',
			'\t}'
			'}'
		]		

		expected = [
			'.class-name {\n',
			'\tfloat: left;',
			'\tposition: absolute;',			
			'\t.another-class-name {\n',
			'\t\tbackground: white',
			'\t\tposition: absolute',			
			'\t}'
			'}'
		]



def main():
	unittest.main()

if __name__ == '__main__':
	main()