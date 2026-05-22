class train:
    def __init__(self,t_name,t_time,t_num):
        self.t_name=t_name
        self.t_time=t_time
        self.t_num=t_num

    def disp_tr(self):
        print(self.t_name,self.t_time,self.t_num,end=' ')

# f1=train('Jharkhan Express','9:30',12058)

class passeg(train):
    def __init__(self, t_name, t_time, t_num,p_name,p_phono,p_add,p_age,p_gender):
        super().__init__(t_name, t_time, t_num)
        self.p_name=p_name
        self.p_phono=p_phono
        self.p_add=p_add
        self.p_age=p_age
        self.p_gender=p_gender
    
    def disp_pas(self):
        super().disp_tr()
        print(self.p_name,self.p_phono,self.p_add,self.p_age,self.p_gender,end=' ')

# f2=passeg('Jharkhan Express','9:30',12058,'Alice','1234567890','123 Main St',25,'Female')

class tick(passeg):
    def __init__(self, t_name, t_time, t_num, p_name, p_phono, p_add, p_age,p_gender,t_pnr,t_seat,t_class,t_price,t_start,t_dest,ti_CNF):
        super().__init__(t_name, t_time, t_num, p_name, p_phono, p_add,p_age,p_gender)
        self.t_pnr=t_pnr
        self.t_seat=t_seat
        self.t_class=t_class
        self.t_price=t_price
        self.t_start=t_start
        self.t_dest=t_dest
        self.ti_CNF=ti_CNF

    def disp_ti(self):
        super().disp_pas()
        print(self.t_pnr,self.t_seat,self.t_class,self.t_price,self.t_start,self.t_dest,self.ti_CNF)

f3=tick('Jharkhan Express','9:30 AM',12058,'Alice','1234567890','123 Main St',25,'Female',1200045,25,'1st AC',4500,'Delhi Junc','Ranchi Junc','CONFIRM')

f3.disp_ti()
