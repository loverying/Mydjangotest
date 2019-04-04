import  sys,os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Mytest.settings")
    import django
    django.setup()


    from backend import main
    interactive_obj = main.ArgvHander(sys.argv)
    host = interactive_obj.call()
    print(host,'ok')
