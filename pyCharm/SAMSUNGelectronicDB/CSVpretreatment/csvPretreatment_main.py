import copExtract
import csvMerge

if __name__ == '__main__':
    csvMr = csvMerge.csvMerge()
    csvMr.start_csvMerge()

    copEx = copExtract.copExtract()
    copEx.start_copExtract()

    print("Job's done")