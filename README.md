# Fake Data  Using  Excel

It takes inputof a excell file with rows having **columns name to generate on 0 index** and **column type to generate on 1 index**.

Sample file name *Related.XLSX* is added.

***Average runtime to generate 1,000 data rows and 13 CSVs is 77.616 seconds***

## USAGE:
1. Clone the repo and add file `fakedatafromexcel.py` to the local prject.
2. Import the project using `from fakedatafromexcel import fakedata`
3. Make the object using `fd = fakedata()`
4. Call the function using `fd.fakedatagenarator(in_path=<path_to_the_excell_file_as_input>)`


##### INPUT PARAMETERS:
Default --> fakedatagenarator(self, in_path, repeat=1000, start_id=1, out_path='output')

      * in_path - (String) Path to the input excel file.
      
      * repeat - (int)[1000 (Default)] Number of rows to generate.
      
      * start_id - (int)[1 (Default)] Index to start from.
      
      * out_path - (String)[output (Default)] Path to create and produce output files.
