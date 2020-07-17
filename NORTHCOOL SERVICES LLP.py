import tkinter as tk


class ColdRoom(tk.Tk):
    """
    This class is having load calculation methods.
    """
    def __init__(self):
        super().__init__()

        tk.Label(self,
                 text="Length").grid(row=1)
        # Length
        self.L = tk.Entry()
        self.L.grid(row=1, column=1)
        # Height
        # Height
        self.H = tk.Entry(self)
        self.H.grid(row=2, column=1)
        # Width
        self.W = tk.Entry(self)
        self.W.grid(row=3, column=1)
        # Ambient Temp °C
        self.AmbiTemp = tk.Entry(self)
        self.AmbiTemp.grid(row=4, column=1)
        # Cold Room Temp °C
        self.ColdRoomTemp = tk.Entry(self)
        self.ColdRoomTemp.grid(row=5, column=1)

        # Product Loading/Incoming Temp. °C
        self.ProductLoading_IncomingTemp = tk.Entry(self)
        self.ProductLoading_IncomingTemp.grid(row=6, column=1)

        tk.Label(self,
                 text="Cold Room Size (Foot)").grid(row=0)
        tk.Label(self,
                 text="Product Load").grid(row=50)
        tk.Label(self,
                 text="Length").grid(row=1)
        tk.Label(self,
                 text="Height").grid(row=2)
        tk.Label(self,
                 text="Width").grid(row=3)
        tk.Label(self,
                 text="Ambient Temp °C").grid(row=4)
        tk.Label(self,
                 text="Cold Room Temp °C").grid(row=5, pady=5)

        tk.Label(self,
                 text="Product Loading \n Incoming Temp °C").grid(row=6, pady=5)

        tk.Button(self,
                  text='Quit',
                  command=self.quit).grid(row=30,
                                          column=0,
                                          pady=10,
                                          )
        tk.Button(self,
                  text='Show', command=self.show_entry_fields).grid(row=30,
                                                                    column=1,
                                                                    pady=5)

        # Dropdown list
        # U value of PUF Panel
        tk.Label(self, text="U value of \n PUF Panel").grid(row=30, column=2, pady=5)
        OptionList_PUF_Panel = [0.2, 0.28]
        self.variable_PUF_Panel = tk.StringVar(self)
        self.variable_PUF_Panel.set(OptionList_PUF_Panel[0])
        self.opt_PUF_Panel = tk.OptionMenu(self, self.variable_PUF_Panel, *OptionList_PUF_Panel).grid(row=30, column=3,
                                                                                                      pady=5)

        # Daily_Loading
        tk.Label(self, text="Daily Loading %").grid(row=30, column=4, pady=5)
        OptionListDaily_Loading = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        self.variable_Daily_Loading = tk.StringVar(self)
        self.variable_Daily_Loading.set(OptionListDaily_Loading[0])
        self.opt_Daily_Loading = tk.OptionMenu(self, self.variable_Daily_Loading, *OptionListDaily_Loading).grid(row=30,
                                                                                                                 column=5,
                                                                                                                 pady=5)

        # ************************************* Model 2 *************************************

        # Product Loading/Incoming Temp. °C
        tk.Label(self, text="Product Loading \n Incoming Temp. °C").grid(row=100, column=0, pady=5)
        OptionListNo_Person_Work_room = [35]
        self.variable_No_Person_Work_room = tk.StringVar(self)
        self.variable_No_Person_Work_room.set(OptionListNo_Person_Work_room[0])
        self.opt_No_Person_Work_room = tk.OptionMenu(self, self.variable_No_Person_Work_room,
                                                     *OptionListNo_Person_Work_room).grid(
            row=100, column=1, pady=5)

        # No. of Person working in Room
        tk.Label(self, text="No. of Person \n working in Room").grid(row=100, column=2, pady=5)
        OptionListNo_Person_Work_room = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.variable_No_Person_Work_room = tk.StringVar(self)
        self.variable_No_Person_Work_room.set(OptionListNo_Person_Work_room[0])
        self.opt_No_Person_Work_room = tk.OptionMenu(self, self.variable_No_Person_Work_room,
                                                     *OptionListNo_Person_Work_room).grid(
            row=100, column=3, pady=5)

        # Heat Rejection Per Person
        tk.Label(self, text="Heat Rejection \n Per Person").grid(row=100, column=4, pady=5)
        OptionListNo_Heat = [300]
        self.variable_Heat = tk.StringVar(self)
        self.variable_Heat.set(OptionListNo_Heat[0])
        self.opt_Heat = tk.OptionMenu(self, self.variable_Heat, *OptionListNo_Heat).grid(row=100, column=5, pady=5)

        # Working Hours
        tk.Label(self, text="Working Hours \n of Person").grid(row=100, column=6, pady=5)
        OptionListWorking_Hours_M2_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.variable_Working_Hours_M2_1 = tk.StringVar(self)
        self.variable_Working_Hours_M2_1.set(OptionListWorking_Hours_M2_1[0])
        self.opt_Working_Hours_M2_1 = tk.OptionMenu(self, self.variable_Working_Hours_M2_1,
                                                    *OptionListWorking_Hours_M2_1).grid(
            row=100,
            column=7,
            pady=5)

        # No. of Lights in Room
        tk.Label(self, text="No.of Lights \n in Room").grid(row=100, column=8, pady=5)
        OptionListNo_Lights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.variable_No_Lights = tk.StringVar(self)
        self.variable_No_Lights.set(OptionListNo_Lights[0])
        self.opt_No_Lights = tk.OptionMenu(self, self.variable_No_Lights, *OptionListNo_Lights).grid(row=100, column=9,
                                                                                                     pady=5)

        # Power Watts/Light
        tk.Label(self, text="Power \n Watts/Light").grid(row=100, column=10, pady=5)
        OptionListPowerWatts = [20, 40, 60, 80, 100, 120, 150, 200]
        self.variable_PowerWatts_Light = tk.StringVar(self)
        self.variable_PowerWatts_Light.set(OptionListPowerWatts[0])
        self.opt_PowerWatts_Light = tk.OptionMenu(self, self.variable_PowerWatts_Light, *OptionListPowerWatts).grid(
            row=100,
            column=11,
            pady=5)

        # Working Hours Light
        tk.Label(self, text="Working Hours \n Light").grid(row=100, column=12, pady=5)
        OptionListWorking_Hours_Light = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
        self.variable_Working_Hours_Light = tk.StringVar(self)
        self.variable_Working_Hours_Light.set(OptionListWorking_Hours_Light[0])
        self.opt_Working_Hours_Heat = tk.OptionMenu(self, self.variable_Working_Hours_Light,
                                                    *OptionListWorking_Hours_Light).grid(
            row=100, column=13, pady=5)

        # ************************************* Model 3 *************************************

        # No. of Evaporator Fans
        tk.Label(self, text="No.of Evaporator \n Fans").grid(row=200, column=0, pady=5)
        OptionListNOEvaporatorFans = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.variable_No_of_EvaporatorFans = tk.StringVar(self)
        self.variable_No_of_EvaporatorFans.set(OptionListNOEvaporatorFans[0])
        self.opt_No_of_Evaporator_Fans = tk.OptionMenu(self, self.variable_No_of_EvaporatorFans,
                                                       *OptionListNOEvaporatorFans).grid(
            row=200, column=1, pady=5)

        # Working Hours Fans
        tk.Label(self, text="Working Hours \n Fans").grid(row=200, column=2, pady=5)
        OptionListWorking_Hours_Fans = [14, 16, 18, 20, 22, 24]
        self.variable_Working_Hours_Fans = tk.StringVar(self)
        self.variable_Working_Hours_Fans.set(OptionListWorking_Hours_Fans[0])
        self.opt_Working_Hours_Fans = tk.OptionMenu(self, self.variable_Working_Hours_Fans,
                                                    *OptionListWorking_Hours_Fans).grid(
            row=200,
            column=3,
            pady=5)

        # Power Watts
        tk.Label(self, text="Power Watts").grid(row=200, column=4, pady=5)
        OptionList_Power_Watts = [50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 400]
        self.variable_Power_Watts = tk.StringVar(self)
        self.variable_Power_Watts.set(OptionList_Power_Watts[0])
        self.opt_Power_Watts = tk.OptionMenu(self, self.variable_Power_Watts, *OptionList_Power_Watts).grid(row=200,
                                                                                                            column=5,
                                                                                                            pady=5)

        # Defrost Heater Power kW
        tk.Label(self, text="Defrost Heater \n Power kW").grid(row=200, column=6, pady=5)
        OptionList_Defrost_Heater_Power_kW = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7]
        self.variable_Defrost_Heater_Power_KW = tk.StringVar(self)
        self.variable_Defrost_Heater_Power_KW.set(OptionList_Defrost_Heater_Power_kW[0])
        self.opt_Defrost_Heater_Power_kW = tk.OptionMenu(self, self.variable_Defrost_Heater_Power_KW,
                                                         *OptionList_Defrost_Heater_Power_kW).grid(row=200, column=7,
                                                                                                   pady=5)

        # Defrost Heater Working Hrs
        tk.Label(self, text="Defrost Heater \n Working Hrs").grid(row=200, column=8, pady=5)
        OptionList_DefrostHeaterWorkingHrs = [0.5, 1, 1.5, 2]
        self.variable_DefrostHeaterWorkingHrs = tk.StringVar(self)
        self.variable_DefrostHeaterWorkingHrs.set(OptionList_DefrostHeaterWorkingHrs[0])
        self.opt_DefrostHeaterWorkingHrs = tk.OptionMenu(self, self.variable_DefrostHeaterWorkingHrs,
                                                         *OptionList_DefrostHeaterWorkingHrs).grid(row=200, column=9,
                                                                                                   pady=5)

        # Defrost Cycles
        tk.Label(self, text="Defrost Cycles").grid(row=200, column=10, pady=5)
        OptionList_DefrostCycles = [1, 2, 3, 4, 5, 6]
        self.variable_DefrostCycles = tk.StringVar(self)
        self.variable_DefrostCycles.set(OptionList_DefrostCycles[0])
        self.opt_DefrostCycles = tk.OptionMenu(self, self.variable_DefrostCycles, *OptionList_DefrostCycles).grid(
            row=200,
            column=11,
            pady=5)

        # Defrost Efficiency
        tk.Label(self, text="Defrost Efficiency").grid(row=200, column=12, pady=5)
        OptionList_DefrostEfficiency = [10, 20, 30, 40]
        self.variable_DefrostEfficiency = tk.StringVar(self)
        self.variable_DefrostEfficiency.set(OptionList_DefrostEfficiency[0])
        self.opt_DefrostEfficiency = tk.OptionMenu(self, self.variable_DefrostEfficiency,
                                                   *OptionList_DefrostEfficiency).grid(
            row=200,
            column=13,
            pady=5)

        # ************************************* Model 4 ************************************

        # Door Opening Per day
        tk.Label(self, text="Door Opening \n Per Day").grid(row=300, column=0, pady=5)
        OptionList_DoorOpeningPerday = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.variable_DoorOpeningPerday = tk.StringVar(self)
        self.variable_DoorOpeningPerday.set(OptionList_DoorOpeningPerday[0])
        self.opt_DoorOpeningPerday = tk.OptionMenu(self, self.variable_DoorOpeningPerday,
                                                   *OptionList_DoorOpeningPerday).grid(
            row=300,
            column=1,
            pady=5)

        # Energy Loss
        tk.Label(self, text="Energy Loss").grid(row=300, column=2, pady=5)
        OptionList_EnergyLoss = [1, 2]
        self.variable_EnergyLoss = tk.StringVar(self)
        self.variable_EnergyLoss.set(OptionList_EnergyLoss[0])
        self.opt_EnergyLoss = tk.OptionMenu(self, self.variable_EnergyLoss, *OptionList_EnergyLoss).grid(row=300,
                                                                                                         column=3,
                                                                                                         pady=5)

        # Product DetailsN
        tk.Label(self, text="Product Details \n Negative").grid(row=300, column=4, pady=5)
        OptionList_ProductDetailsN = ['Negative', 'Grapes', 'Limes', 'Lemon', 'Mango', 'Orange', 'Pomegranate',
                                      'Strawberry',
                                      'Broccoli', 'Cucumber', 'Eggplant', 'Cauliflower',
                                      'Garlic', 'Carrot', 'Cabbage', 'Mushroom', 'Onion', 'Potato', 'Tomato', 'Milk',
                                      'Butter',
                                      'Cheese', 'Paneer', 'Eggs']
        self.variable_ProductDetailsN = tk.StringVar(self)
        self.variable_ProductDetailsN.set(OptionList_ProductDetailsN[0])
        self.opt_ProductDetailsN = tk.OptionMenu(self, self.variable_ProductDetailsN, *OptionList_ProductDetailsN).grid(
            row=300,
            column=5,
            pady=5)

        # Product DetailsP
        tk.Label(self, text="Product Details \n Positive").grid(row=300, column=6, pady=5)
        OptionList_ProductDetailsP = ['Positive', 'Chicken', 'IceCream', 'Fish', 'Meat']
        self.variable_ProductDetailsP = tk.StringVar(self)
        self.variable_ProductDetailsP.set(OptionList_ProductDetailsP[0])
        self.opt_ProductDetailsP = tk.OptionMenu(self, self.variable_ProductDetailsP, *OptionList_ProductDetailsP).grid(
            row=300,
            column=7,
            pady=5)

        # Conversion Factor KJ to kWh
        tk.Label(self, text="Conversion Factor \n KJ to kWh").grid(row=300, column=8, pady=5)
        self.OptionLis_ConversionFactor = [3600]
        self.variable_ConversionFactor = tk.StringVar(self)
        self.variable_ConversionFactor.set(self.OptionLis_ConversionFactor[0])
        self.opt_ConversionFactor = tk.OptionMenu(self, self.variable_ConversionFactor,
                                                  *self.OptionLis_ConversionFactor).grid(
            row=300,
            column=9,
            pady=5)

        self.Product_Details_Negative = {'Negative': 0, 'Grapes': 3.71, 'Limes': 3.93, 'Lemon': 3.93, 'Mango': 3.74,
                                         'Orange': 3.81,
                                         'Pomegranate': 3.7, 'Strawberry': 4, 'Broccoli': 4.01, 'Cucumber': 4.09,
                                         'Eggplant': 4.02,
                                         'Cauliflower': 4.02, 'Garlic': 3.17, 'Carrot': 3.92, 'Cabbage': 4.02,
                                         'Mushroom': 3.99,
                                         'Onion': 3.95, 'Potato': 3.67, 'Tomato': 4.08, 'Milk': 3.89, 'Butter': 2.4,
                                         'Cheese': 3.34,
                                         'Paneer': 3.3, 'Eggs': 3.63}
        self.Product_Details_Negative_Product_RSH_LH = {'Negative': 0.0, 'Grapes': 1.9, 'Limes': 2.0, 'Lemon': 2.0,
                                                        'Mango': 1.9,
                                                        'Orange': 1.9,
                                                        'Pomegranate': 1.9, 'Strawberry': 2.0, 'Broccoli': 2.0,
                                                        'Cucumber': 2.0,
                                                        'Eggplant': 2.0,
                                                        'Cauliflower': 2.0, 'Garlic': 1.6, 'Carrot': 2.0,
                                                        'Cabbage': 2.0,
                                                        'Mushroom': 2.0,
                                                        'Onion': 2.0, 'Potato': 1.8, 'Tomato': 2.0, 'Milk': 1.9,
                                                        'Butter': 1.2,
                                                        'Cheese': 1.7,
                                                        'Paneer': 2.6, 'Eggs': 2.7}
        self.OptionList_ProductDetails_Positive = {'Positive': 0, 'Chicken': 3.53, 'IceCream': 3.22, 'Fish': 3.83,
                                                   'Meat': 3.62}
        self.OptionList_ProductDetails_Positive_Latent_Heat = {'Positive': 0, 'Chicken': 0.3, 'IceCream': 0.2,
                                                               'Fish': 0.3,
                                                               'Meat': 0.3}

    def formulas_calculation(self):
        """
        This method is used to calculate the different formulas.
        """
        # This method is given abstract due to company policies.
        pass
        

        

    def show_entry_fields(self):
        """
        This method is invoke as soon as the show button is clicked
        :return:
        """
        self.formulas_calculation()
        tk.Label(self, text="Length   " + self.L.get()).grid(row=1, column=2, pady=5)
        tk.Label(self, text="Height   " + self.H.get()).grid(row=2, column=2, pady=5)
        tk.Label(self, text="Width    " + self.W.get()).grid(row=3, column=2, pady=5)
        tk.Label(self, text="Length in meters    " + format('%.2f' % self.Le)).grid(row=1, column=3, pady=5)
        tk.Label(self, text="Height in meters    " + format('%.2f' % self.He)).grid(row=2, column=3, pady=5)
        tk.Label(self, text="Width in meters    " + format('%.2f' % self.We)).grid(row=3, column=3, pady=5)

        tk.Label(self, text="Daily Loading %    " + (format('%.1f' % round(self.Daily_Loading)))).grid(row=30, column=6,
                                                                                                       pady=5)
        tk.Label(self, text="Transmission Load Δ T    " + (format('%.1f' % round(self.TransmissionLoad_Temp)))).grid(
            row=5,
            column=2,
            pady=5)
        tk.Label(self, text="Transmission Load Δ T    " + (format('%.2f' % self.Transmission_Load))).grid(row=450,
                                                                                                          column=2,
                                                                                                          pady=5)

        tk.Label(self, text="Wall celling \n Area m²").grid(row=1, column=4, pady=5)
        readOnlyText_Wall_celling_Area = tk.Entry(self)
        readOnlyText_Wall_celling_Area.insert(1, format('%.1f' % self.Wall_ceiling_Area_msq))
        readOnlyText_Wall_celling_Area.configure(state='disabled')
        readOnlyText_Wall_celling_Area.grid(row=1, column=5, pady=5)

        tk.Label(self, text="Floor Area \n  m² (MTR)").grid(row=2, column=4, pady=5)
        readOnlyText_Floor_Area = tk.Entry(self)
        readOnlyText_Floor_Area.insert(1, (format('%.1f' % self.Floor_Area_msq)))
        readOnlyText_Floor_Area.configure(state='disabled')
        readOnlyText_Floor_Area.grid(row=2, column=5, pady=5)

        tk.Label(self, text="Volume m³ \n  (MTR)").grid(row=3, column=4, pady=5)
        readOnlyText_Volume_Area = tk.Entry(self)
        readOnlyText_Volume_Area.insert(1, (format('%.1f' % self.Volume__msq)))
        readOnlyText_Volume_Area.configure(state='disabled')
        readOnlyText_Volume_Area.grid(row=3, column=5, pady=5)

        tk.Label(self, text="Volume ft³").grid(row=4, column=4, pady=5)
        readOnlyText_Volume_Ft = tk.Entry(self)
        readOnlyText_Volume_Ft.insert(1, (format('%.1f' % self.Volume_ft)))
        readOnlyText_Volume_Ft.configure(state='disabled')
        readOnlyText_Volume_Ft.grid(row=4, column=5, pady=5)

        tk.Label(self, text="Room Net \n Capacity Kg").grid(row=5, column=4, pady=5)
        readOnlyText_Room_Net_Capacity = tk.Entry(self)
        readOnlyText_Room_Net_Capacity.insert(1, format('%.1f' % self.Room_Net_Capacity_Kg))
        readOnlyText_Room_Net_Capacity.configure(state='disabled')
        readOnlyText_Room_Net_Capacity.grid(row=5, column=5, pady=5)

        # Air Infiltration Δ T
        tk.Label(self, text="Air Infiltration Δ T").grid(row=300, column=10, pady=5)
        readOnlyText_Air_Infiltration_T = tk.Entry(self)
        readOnlyText_Air_Infiltration_T.insert(1, self.AirInfiltration_T)
        readOnlyText_Air_Infiltration_T.configure(state='disabled')
        readOnlyText_Air_Infiltration_T.grid(row=300, column=11, pady=5)

        # Specific Heat \n  Negative
        user_negative_select_item_negative = self.variable_ProductDetailsN.get()
        if user_negative_select_item_negative in self.Product_Details_Negative and user_negative_select_item_negative in self.Product_Details_Negative_Product_RSH_LH:
            print(self.Product_Details_Negative[user_negative_select_item_negative],
                  self.Product_Details_Negative_Product_RSH_LH[user_negative_select_item_negative])

        # Specific Heat Negative
        tk.Label(self, text="Specific Heat \n  Negative").grid(row=350, column=4, pady=5)
        readOnlyText_NEGATIVE = tk.Entry(self)
        readOnlyText_NEGATIVE.insert(1, self.Product_Details_Negative[user_negative_select_item_negative])
        readOnlyText_NEGATIVE.configure(state='disabled')
        readOnlyText_NEGATIVE.grid(row=350, column=5)

        # Product RSH/LH
        tk.Label(self, text="Product RSH/LH").grid(row=400, column=4, pady=5)
        readOnlyText_Product_RSH_LH = tk.Entry(self)
        readOnlyText_Product_RSH_LH.insert(1,
                                           self.Product_Details_Negative_Product_RSH_LH[
                                               user_negative_select_item_negative])
        readOnlyText_Product_RSH_LH.configure(state='disabled')
        readOnlyText_Product_RSH_LH.grid(row=400, column=5)

        # Specific Heat Positive
        user_negative_select_item_positive = self.variable_ProductDetailsP.get()
        if user_negative_select_item_positive in self.OptionList_ProductDetails_Positive and user_negative_select_item_positive in self.OptionList_ProductDetails_Positive_Latent_Heat:
            print(self.OptionList_ProductDetails_Positive[user_negative_select_item_positive],
                  self.OptionList_ProductDetails_Positive_Latent_Heat[user_negative_select_item_positive])

        # Specific Heat Positive
        tk.Label(self, text="Specific Heat \n  Positive").grid(row=350, column=6, pady=5)
        readOnlyText_POSSITIVE = tk.Entry(self)
        readOnlyText_POSSITIVE.insert(1, self.OptionList_ProductDetails_Positive[user_negative_select_item_positive])
        readOnlyText_POSSITIVE.configure(state='disabled')
        readOnlyText_POSSITIVE.grid(row=350, column=7)

        # Latent Heat
        tk.Label(self, text="Latent Heat").grid(row=400, column=6, pady=5)
        readOnlyText_Latent_Heat = tk.Entry(self)
        readOnlyText_Latent_Heat.insert(1,
                                        self.OptionList_ProductDetails_Positive_Latent_Heat[
                                            user_negative_select_item_positive])
        readOnlyText_Latent_Heat.configure(state='disabled')
        readOnlyText_Latent_Heat.grid(row=400, column=7)


if __name__ == "__main__":
    app = ColdRoom()
    app.title("My COLD ROOM app")
    app.mainloop()
