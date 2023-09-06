growth = [3, 1, 2, 4, 2, 3, 2]
growth.sort()
smallest_growth = growth[0]
print(f'The smallest growth in the week is: {smallest_growth}cm')

biggest_growth = growth[len(growth) - 1]
print(f'The biggest growth in the week is: {biggest_growth}cm')

average_growth = sum(growth) / len(growth)
print(f'The average growth in the week is: {average_growth}cm')

new_growth = [2, 0, 3, 2, 4, 5, 5]
joined_growth = growth + new_growth
joined_smallest_growth = min(joined_growth)
print(f'The smallest growth in these 2 weeks is: {joined_smallest_growth}cm')

joined_biggest_growth = max(joined_growth)
print(f'The biggest growth in these 2 weeks is: {joined_biggest_growth}cm')

joined_average_growth = sum(joined_growth) / len(joined_growth)
print(f'The average growth in these 2 weeks is: {joined_average_growth}cm')

joined_smallest_growth_count = joined_growth.count(joined_smallest_growth)
print(f'The smallest growth happened {joined_smallest_growth_count} times in these 2 weeks')

joined_biggest_growth_count = joined_growth.count(joined_biggest_growth)
print(f'The biggest growth happened {joined_biggest_growth_count} times in these 2 weeks')

# PL--------------------------------------------------------------------------------------------

wzrost = [3, 1, 2, 4, 2, 3, 2]
wzrost.sort()
najmniejszy_wzrost = wzrost[0]
print(f'Najmniejszy wzrost w ciągu tygodnia wynosi: {najmniejszy_wzrost} cm')

najwiekszy_wzrost = wzrost[len(wzrost) - 1]
print(f'Największy wzrost w ciągu tygodnia wynosi: {najwiekszy_wzrost} cm')

sredni_wzrost = sum(wzrost) / len(wzrost)
print(f'Średni wzrost w ciągu tygodnia wynosi: {sredni_wzrost} cm')

nowy_wzrost = [2, 0, 3, 2, 4, 5, 5]
polaczony_wzrost = wzrost + nowy_wzrost
najmniejszy_polaczony_wzrost = min(polaczony_wzrost)
print(f'Najmniejszy wzrost w ciągu tych 2 tygodni wynosi: {najmniejszy_polaczony_wzrost} cm')

najwiekszy_polaczony_wzrost = max(polaczony_wzrost)
print(f'Największy wzrost w ciągu tych 2 tygodni wynosi: {najwiekszy_polaczony_wzrost} cm')

sredni_polaczony_wzrost = sum(polaczony_wzrost) / len(polaczony_wzrost)
print(f'Średni wzrost w ciągu tych 2 tygodni wynosi: {sredni_polaczony_wzrost} cm')

liczba_najmniejszych_wzrostow = polaczony_wzrost.count(najmniejszy_polaczony_wzrost)
print(f'Najmniejszy wzrost wystąpił {liczba_najmniejszych_wzrostow} razy w ciągu tych 2 tygodni')

liczba_najwiekszych_wzrostow = polaczony_wzrost.count(najwiekszy_polaczony_wzrost)
print(f'Największy wzrost wystąpił {liczba_najwiekszych_wzrostow} razy w ciągu tych 2 tygodni')
