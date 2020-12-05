import FileIO

dataset1 = FileIO.get_all_file_path('dataset/test_audio_16', 'wav')
dataset2 = FileIO.get_all_file_path('dataset/test_audio_16_kmj', 'wav')

filepath = 'convert_dataset'
for data in dataset1:
    filename = FileIO.get_pure_filename(data)
    filename = int(filename)+1000

    new_filename = '{}/{}.wav'.format(filepath, filename)
    FileIO.convert_filename(data, new_filename)

for data in dataset2:
    filename = FileIO.get_pure_filename(data)
    filename = int(filename)+2000

    new_filename = '{}/{}.wav'.format(filepath, filename)
    FileIO.convert_filename(data, new_filename)
