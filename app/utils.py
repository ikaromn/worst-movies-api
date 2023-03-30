from collections import defaultdict


def get_producer_win_intervals(movies):
    """
    Receives a list of movies that win a prize.
    Return a JSON with two keys:
      - max: Contains a list of producers that takes more time to win another prize
      - min: Contains a list of producers that takes less time to win another prize
    """

    producers = defaultdict(list)
    for name, year in movies:
         producers[name].append(year)

    min_intervals = []
    max_intervals = []

    for name, years in producers.items():
        sorted_years = sorted(years)
        num_wins = len(sorted_years)

        # Calculate each interval beetween the years
        intervals = [sorted_years[i+1] - sorted_years[i] for i in range(num_wins-1)]

        # Get the minimum and maximum interval
        min_interval = min(intervals)
        max_interval = max(intervals)

        # Get the index of each interval to access the year
        min_year_index = intervals.index(min_interval)
        max_year_index = intervals.index(max_interval)
        min_interval_data = {
            "producer": name,
            "interval": min_interval,
            "previousWin": sorted_years[min_year_index],
            "followingWin": sorted_years[min_year_index+1],
        }
        max_interval_data = {
            "producer": name,
            "interval": max_interval,
            "previousWin": sorted_years[max_year_index],
            "followingWin": sorted_years[max_year_index+1],
        }
        min_intervals.append(min_interval_data)
        max_intervals.append(max_interval_data)

    min_intervals = sorted(min_intervals, key=lambda x: x["interval"])
    max_intervals = sorted(max_intervals, key=lambda x: x["interval"], reverse=True)

    return {"min": min_intervals, "max": max_intervals}
