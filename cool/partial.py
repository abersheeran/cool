from functools import partial as _partial


class partial(_partial):
    def __call__(self, *args, **keywords):
        args_iter = iter(args)
        return self.func(
            *map(lambda arg: (next(args_iter) if arg == ... else arg), self.args),
            *args_iter,
            **{**self.keywords, **keywords}
        )
