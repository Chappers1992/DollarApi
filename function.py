

class NewTask:
    @staticmethod
    def generate_commandline(task, mu, proc_date, start_date, args):
        return f'CMD BLAH BLAH {task} running on {mu} -P {proc_date} -s {start_date} -a {args} '