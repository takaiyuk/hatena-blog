def calc_posession(FGA: int, TO: int, FTA: int, OR: int) -> float:
    """
    ref. https://www.nbastuffer.com/analytics101/possession/
    - FGA: Field Goal Attempts
    - TO: Turnovers
    - FTA: Free Throw Attempts
    - OR: Offensive Rebounds
    """
    return 0.96 * (FGA + TO + 0.44 * FTA - OR)
