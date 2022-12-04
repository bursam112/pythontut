import shutil

for file in range(1, 421):
    try:
        shutil.copy(f'C:\\Users\\bulle\\Downloads\\infinitefusion_5.0.36.3-full\\Graphics\\CustomBattlers\\{file}.6.png',
                    f'C:\\Users\\bulle\\OneDrive\\Desktop\\coolpok\\{file}.6.png')

    except FileNotFoundError:
        pass

print('Done!')
