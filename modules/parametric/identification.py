from points import *

class Identification:
    def __init__(self):
        self.count_bees = 10
        self.fails_limit = 10

        self.mcn_max = 30_000
        self.mcn_current = 1

    def execute(self):
        point_result = None
        generator = Generator()
        point_factory = PointFactory(generator, DeltaFactory(Delta))

        point_factory_initial = PointFactory(
            Generator()->set_expr(PointSeekerInitial()),
            DeltaFactory(Delta)
        )

        """
        Формуємо набір початкових значень
        """
        # Знаходження початкових точок по формулі 11
        points_initial = point_factory_initial.make(self.count_bees)

        # Формуємо ще 10 точок для селекції
        generator.set_expr(PointSeeker(points_initial))
        points = point_factory.make(self.count_bees)

        # Виконуємо попарну селекцію точок - обираємо одну із двох, дельта якої менша
        for point in points:
            point_initial = points_initial.get(point.key)
            if point_initial.delta < point.delta:
                points.replace(point_initial)

        """
        Run process
        """
        generator.set_expr(PointSeeker(points))

        while self.mcn_current <= self.mcn_max:
            for point in points:

                check_near_points = 1

                if check_near_points > 0:
                    for _ in range(check_near_points):
                        near_point = point_factory.make_one(point.key)
                        if point.delta > near_point.delta:
                            points.replace(near_point)
                        else:
                            point.fails += 1
                else:
                    new_point = point_factory_initial.make_one(point.key)
                    points.replace(new_point)

                if point.fails >= self.fails_limit:
                    new_point = point_factory_initial.make_one(point.key)
                    points.replace(new_point)

                if point.delta == 0:
                    point_result = point
                    break

            else:
                continue

            break

            self.mcn_current += 1

        return point_result, self.mcn_current
