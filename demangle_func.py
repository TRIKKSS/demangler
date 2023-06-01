from elftools.elf.elffile import ELFFile
from elftools.elf.sections import (
    SymbolTableSection, SymbolTableIndexSection
)
import sys

def get_symbols(binary):
	functions = []
	with open(binary, 'rb') as f:
		elf = ELFFile(f)
		symbol_tables = [(idx, s) for idx, s in enumerate(elf.iter_sections()) if isinstance(s, SymbolTableSection)]
		for section_index, section in symbol_tables:
			for nsym, symbol in enumerate(section.iter_symbols()):
				# print(symbol.name)
				functions.append(symbol.name)
	return functions

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print(f"usage : {sys.argv[0]} [elf/lib]")
		exit(1)

	for i in get_symbols(sys.argv[1]):
		print(i)