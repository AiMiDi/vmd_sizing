#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# generated by wxGlade 0.9.2 on Thu Mar 21 10:05:00 2019
#
# マウス右ダブルクリックで該当色を”(r, g, b)”でクリップボードにコピー
import wx

# begin wxGlade: dependencies
# end wxGlade
# begin wxGlade: extracode
# end wxGlade
class MyFrame(wx.Frame):
     def __init__(self, *args, **kwds):
          # begin wxGlade: MyFrame.__init__
          kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
          wx.Frame.__init__(self, *args, **kwds)
          self.SetSize((900, 800))
          self.__set_properties()
          self.__do_layout()
          # end wxGlade
     def __set_properties(self):
          # begin wxGlade: MyFrame.__set_properties
          self.SetTitle("wx.ColourDatabase")
          # end wxGlade
     def __do_layout(self):
          # begin wxGlade: MyFrame.__do_layout
          sizer_1 = wx.BoxSizer(wx.VERTICAL)
          sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
          sizer_6 = wx.BoxSizer(wx.VERTICAL)
          sizer_5 = wx.BoxSizer(wx.VERTICAL)
          sizer_4 = wx.BoxSizer(wx.VERTICAL)
          sizer_3 = wx.BoxSizer(wx.VERTICAL)
          label_69 = wx.StaticText(self, wx.ID_ANY, "　　＊＊　鼠标右键点击可将相应颜色（r，g，b）复制到剪贴板　＊＊")
          sizer_1.Add(label_69, 0, wx.ALL | wx.EXPAND, 1)
          label_70 = wx.StaticText(
               self, wx.ID_ANY, "AQUAMARINE", style=wx.ALIGN_CENTER)
          label_70.SetBackgroundColour(wx.Colour("AQUAMARINE"))
          label_70.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_3.Add(label_70, 0, wx.ALL | wx.EXPAND, 1)
          label_2 = wx.StaticText(
               self, wx.ID_ANY, "BLACK", style=wx.ALIGN_CENTER)
          label_2.SetBackgroundColour(wx.Colour("BLACK"))
          label_2.SetForegroundColour(wx.Colour(255, 255, 255))
          sizer_3.Add(label_2, 0, wx.ALL | wx.EXPAND, 1)
          label_71 = wx.StaticText(
               self, wx.ID_ANY, "BLUE", style=wx.ALIGN_CENTER)
          label_71.SetBackgroundColour(wx.Colour("BLUE"))
          label_71.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_3.Add(label_71, 0, wx.ALL | wx.EXPAND, 1)
          label_72 = wx.StaticText(
               self, wx.ID_ANY, "BLUE VIOLET", style=wx.ALIGN_CENTER)
          label_72.SetBackgroundColour(wx.Colour("BLUE VIOLET"))
          label_72.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_3.Add(label_72, 0, wx.ALL | wx.EXPAND, 1)
          label_73 = wx.StaticText(
               self, wx.ID_ANY, "BROWN", style=wx.ALIGN_CENTER)
          label_73.SetBackgroundColour(wx.Colour("BROWN"))
          label_73.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_3.Add(label_73, 0, wx.ALL | wx.EXPAND, 1)
          label_74 = wx.StaticText(
               self, wx.ID_ANY, "CADET BLUE", style=wx.ALIGN_CENTER)
          label_74.SetBackgroundColour(wx.Colour("CADET BLUE"))
          label_74.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_3.Add(label_74, 0, wx.ALL | wx.EXPAND, 1)
          label_75 = wx.StaticText(
               self, wx.ID_ANY, "CORAL", style=wx.ALIGN_CENTER)
          label_75.SetBackgroundColour(wx.Colour("CORAL"))
          label_75.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_3.Add(label_75, 0, wx.ALL | wx.EXPAND, 1)
          label_76 = wx.StaticText(
               self, wx.ID_ANY, "CORNFLOWER BLUE", style=wx.ALIGN_CENTER)
          label_76.SetBackgroundColour(wx.Colour("CORNFLOWER BLUE"))
          label_76.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_3.Add(label_76, 0, wx.ALL | wx.EXPAND, 1)
          label_77 = wx.StaticText(
               self, wx.ID_ANY, "CYAN", style=wx.ALIGN_CENTER)
          label_77.SetBackgroundColour(wx.Colour("CYAN"))
          label_77.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_3.Add(label_77, 0, wx.ALL | wx.EXPAND, 1)
          label_78 = wx.StaticText(
               self, wx.ID_ANY, "DARK GREY", style=wx.ALIGN_CENTER)
          label_78.SetBackgroundColour(wx.Colour("DARK GREY"))
          label_78.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_3.Add(label_78, 0, wx.ALL | wx.EXPAND, 1)
          label_79 = wx.StaticText(
               self, wx.ID_ANY, "DARK GREEN", style=wx.ALIGN_CENTER)
          label_79.SetBackgroundColour(wx.Colour("DARK GREEN"))
          label_79.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_3.Add(label_79, 0, wx.ALL | wx.EXPAND, 1)
          label_80 = wx.StaticText(
               self, wx.ID_ANY, "DARK OLIVE GREEN", style=wx.ALIGN_CENTER)
          label_80.SetBackgroundColour(wx.Colour("DARK OLIVE GREEN"))
          label_80.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_3.Add(label_80, 0, wx.ALL | wx.EXPAND, 1)
          label_81 = wx.StaticText(
               self, wx.ID_ANY, "DARK ORCHID", style=wx.ALIGN_CENTER)
          label_81.SetBackgroundColour(wx.Colour("DARK ORCHID"))
          label_81.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_3.Add(label_81, 0, wx.ALL | wx.EXPAND, 1)
          label_82 = wx.StaticText(
               self, wx.ID_ANY, "DARK SLATE BLUE", style=wx.ALIGN_CENTER)
          label_82.SetBackgroundColour(wx.Colour("DARK SLATE BLUE"))
          label_82.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_3.Add(label_82, 0, wx.ALL | wx.EXPAND, 1)
          label_83 = wx.StaticText(
               self, wx.ID_ANY, "DARK SLATE GREY", style=wx.ALIGN_CENTER)
          label_83.SetBackgroundColour(wx.Colour("DARK SLATE GREY"))
          label_83.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_3.Add(label_83, 0, wx.ALL | wx.EXPAND, 1)
          label_84 = wx.StaticText(
               self, wx.ID_ANY, "DARK TURQUOISE", style=wx.ALIGN_CENTER)
          label_84.SetBackgroundColour(wx.Colour("DARK TURQUOISE"))
          label_84.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_3.Add(label_84, 0, wx.ALL | wx.EXPAND, 1)
          label_85 = wx.StaticText(
               self, wx.ID_ANY, "DIM GREY", style=wx.ALIGN_CENTER)
          label_85.SetBackgroundColour(wx.Colour("DIM GREY"))
          label_85.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_3.Add(label_85, 0, wx.ALL | wx.EXPAND, 1)
          sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
          label_86 = wx.StaticText(
               self, wx.ID_ANY, "FIREBRICK", style=wx.ALIGN_CENTER)
          label_86.SetBackgroundColour(wx.Colour("FIREBRICK"))
          label_86.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_4.Add(label_86, 0, wx.ALL | wx.EXPAND, 1)
          label_102 = wx.StaticText(
               self, wx.ID_ANY, "FOREST GREEN", style=wx.ALIGN_CENTER)
          label_102.SetBackgroundColour(wx.Colour("FOREST GREEN"))
          label_102.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_4.Add(label_102, 0, wx.ALL | wx.EXPAND, 1)
          label_87 = wx.StaticText(
               self, wx.ID_ANY, "GOLD", style=wx.ALIGN_CENTER)
          label_87.SetBackgroundColour(wx.Colour("GOLD"))
          label_87.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_4.Add(label_87, 0, wx.ALL | wx.EXPAND, 1)
          label_88 = wx.StaticText(
               self, wx.ID_ANY, "GOLDENROD", style=wx.ALIGN_CENTER)
          label_88.SetBackgroundColour(wx.Colour("GOLDENROD"))
          label_88.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_4.Add(label_88, 0, wx.ALL | wx.EXPAND, 1)
          label_89 = wx.StaticText(
               self, wx.ID_ANY, "GREY", style=wx.ALIGN_CENTER)
          label_89.SetBackgroundColour(wx.Colour("GREY"))
          label_89.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_4.Add(label_89, 0, wx.ALL | wx.EXPAND, 1)
          label_90 = wx.StaticText(
               self, wx.ID_ANY, "GREEN", style=wx.ALIGN_CENTER)
          label_90.SetBackgroundColour(wx.Colour("GREEN"))
          label_90.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_4.Add(label_90, 0, wx.ALL | wx.EXPAND, 1)
          label_91 = wx.StaticText(
               self, wx.ID_ANY, "GREEN YELLOW", style=wx.ALIGN_CENTER)
          label_91.SetBackgroundColour(wx.Colour("GREEN YELLOW"))
          label_91.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_4.Add(label_91, 0, wx.ALL | wx.EXPAND, 1)
          label_92 = wx.StaticText(
               self, wx.ID_ANY, "INDIAN RED", style=wx.ALIGN_CENTER)
          label_92.SetBackgroundColour(wx.Colour("INDIAN RED"))
          label_92.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_4.Add(label_92, 0, wx.ALL | wx.EXPAND, 1)
          label_93 = wx.StaticText(
               self, wx.ID_ANY, "KHAKI", style=wx.ALIGN_CENTER)
          label_93.SetBackgroundColour(wx.Colour("KHAKI"))
          label_93.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_4.Add(label_93, 0, wx.ALL | wx.EXPAND, 1)
          label_94 = wx.StaticText(
               self, wx.ID_ANY, "LIGHT BLUE", style=wx.ALIGN_CENTER)
          label_94.SetBackgroundColour(wx.Colour("LIGHT BLUE"))
          label_94.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_4.Add(label_94, 0, wx.ALL | wx.EXPAND, 1)
          label_95 = wx.StaticText(
               self, wx.ID_ANY, "LIGHT GREY", style=wx.ALIGN_CENTER)
          label_95.SetBackgroundColour(wx.Colour("LIGHT GREY"))
          label_95.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_4.Add(label_95, 0, wx.ALL | wx.EXPAND, 1)
          label_96 = wx.StaticText(
               self, wx.ID_ANY, "LIGHT STEEL BLUE", style=wx.ALIGN_CENTER)
          label_96.SetBackgroundColour(wx.Colour("LIGHT STEEL BLUE"))
          label_96.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_4.Add(label_96, 0, wx.ALL | wx.EXPAND, 1)
          label_97 = wx.StaticText(
               self, wx.ID_ANY, "LIME GREEN", style=wx.ALIGN_CENTER)
          label_97.SetBackgroundColour(wx.Colour("LIME GREEN"))
          label_97.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_4.Add(label_97, 0, wx.ALL | wx.EXPAND, 1)
          label_98 = wx.StaticText(
               self, wx.ID_ANY, "MAGENTA", style=wx.ALIGN_CENTER)
          label_98.SetBackgroundColour(wx.Colour("MAGENTA"))
          label_98.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_4.Add(label_98, 0, wx.ALL | wx.EXPAND, 1)
          label_99 = wx.StaticText(
               self, wx.ID_ANY, "MAROON", style=wx.ALIGN_CENTER)
          label_99.SetBackgroundColour(wx.Colour("MAROON"))
          label_99.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_4.Add(label_99, 0, wx.ALL | wx.EXPAND, 1)
          label_100 = wx.StaticText(
               self, wx.ID_ANY, "MEDIUM AQUAMARINE", style=wx.ALIGN_CENTER)
          label_100.SetBackgroundColour(wx.Colour("MEDIUM AQUAMARINE"))
          label_100.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_4.Add(label_100, 0, wx.ALL | wx.EXPAND, 1)
          label_101 = wx.StaticText(
               self, wx.ID_ANY, "MEDIUM BLUE", style=wx.ALIGN_CENTER)
          label_101.SetBackgroundColour(wx.Colour("MEDIUM BLUE"))
          label_101.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_4.Add(label_101, 0, wx.ALL | wx.EXPAND, 1)
          sizer_2.Add(sizer_4, 1, wx.EXPAND, 0)
          label_103 = wx.StaticText(
               self, wx.ID_ANY, "MEDIUM FOREST GREEN", style=wx.ALIGN_CENTER)
          label_103.SetBackgroundColour(wx.Colour("MEDIUM FOREST GREEN"))
          label_103.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_5.Add(label_103, 0, wx.ALL | wx.EXPAND, 1)
          label_104 = wx.StaticText(
               self, wx.ID_ANY, "MEDIUM GOLDENROD", style=wx.ALIGN_CENTER)
          label_104.SetBackgroundColour(wx.Colour("MEDIUM GOLDENROD"))
          label_104.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_5.Add(label_104, 0, wx.ALL | wx.EXPAND, 1)
          label_105 = wx.StaticText(
               self, wx.ID_ANY, "MEDIUM ORCHID", style=wx.ALIGN_CENTER)
          label_105.SetBackgroundColour(wx.Colour("MEDIUM ORCHID"))
          label_105.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_5.Add(label_105, 0, wx.ALL | wx.EXPAND, 1)
          label_106 = wx.StaticText(
               self, wx.ID_ANY, "MEDIUM SEA GREEN", style=wx.ALIGN_CENTER)
          label_106.SetBackgroundColour(wx.Colour("MEDIUM SEA GREEN"))
          label_106.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_5.Add(label_106, 0, wx.ALL | wx.EXPAND, 1)
          label_107 = wx.StaticText(
               self, wx.ID_ANY, "MEDIUM SLATE BLUE", style=wx.ALIGN_CENTER)
          label_107.SetBackgroundColour(wx.Colour("MEDIUM SLATE BLUE"))
          label_107.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_5.Add(label_107, 0, wx.ALL | wx.EXPAND, 1)
          label_108 = wx.StaticText(
               self, wx.ID_ANY, "MEDIUM SPRING GREEN", style=wx.ALIGN_CENTER)
          label_108.SetBackgroundColour(wx.Colour("MEDIUM SPRING GREEN"))
          label_108.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_5.Add(label_108, 0, wx.ALL | wx.EXPAND, 1)
          label_109 = wx.StaticText(
               self, wx.ID_ANY, "MEDIUM TURQUOISE", style=wx.ALIGN_CENTER)
          label_109.SetBackgroundColour(wx.Colour("MEDIUM TURQUOISE"))
          label_109.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_5.Add(label_109, 0, wx.ALL | wx.EXPAND, 1)
          label_110 = wx.StaticText(
               self, wx.ID_ANY, "MEDIUM VIOLET RED", style=wx.ALIGN_CENTER)
          label_110.SetBackgroundColour(wx.Colour("MEDIUM VIOLET RED"))
          label_110.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_5.Add(label_110, 0, wx.ALL | wx.EXPAND, 1)
          label_111 = wx.StaticText(
               self, wx.ID_ANY, "MIDNIGHT BLUE", style=wx.ALIGN_CENTER)
          label_111.SetBackgroundColour(wx.Colour("MIDNIGHT BLUE"))
          label_111.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_5.Add(label_111, 0, wx.ALL | wx.EXPAND, 1)
          label_112 = wx.StaticText(
               self, wx.ID_ANY, "NAVY", style=wx.ALIGN_CENTER)
          label_112.SetBackgroundColour(wx.Colour("NAVY"))
          label_112.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_5.Add(label_112, 0, wx.ALL | wx.EXPAND, 1)
          label_113 = wx.StaticText(
               self, wx.ID_ANY, "ORANGE", style=wx.ALIGN_CENTER)
          label_113.SetBackgroundColour(wx.Colour("ORANGE"))
          label_113.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_5.Add(label_113, 0, wx.ALL | wx.EXPAND, 1)
          label_114 = wx.StaticText(
               self, wx.ID_ANY, "ORANGE RED", style=wx.ALIGN_CENTER)
          label_114.SetBackgroundColour(wx.Colour("ORANGE RED"))
          label_114.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_5.Add(label_114, 0, wx.ALL | wx.EXPAND, 1)
          label_115 = wx.StaticText(
               self, wx.ID_ANY, "ORCHID", style=wx.ALIGN_CENTER)
          label_115.SetBackgroundColour(wx.Colour("ORCHID"))
          label_115.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_5.Add(label_115, 0, wx.ALL | wx.EXPAND, 1)
          label_116 = wx.StaticText(
               self, wx.ID_ANY, "PALE GREEN", style=wx.ALIGN_CENTER)
          label_116.SetBackgroundColour(wx.Colour("PALE GREEN"))
          label_116.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_5.Add(label_116, 0, wx.ALL | wx.EXPAND, 1)
          label_117 = wx.StaticText(
               self, wx.ID_ANY, "PINK", style=wx.ALIGN_CENTER)
          label_117.SetBackgroundColour(wx.Colour("PINK"))
          label_117.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_5.Add(label_117, 0, wx.ALL | wx.EXPAND, 1)
          label_118 = wx.StaticText(
               self, wx.ID_ANY, "PLUM", style=wx.ALIGN_CENTER)
          label_118.SetBackgroundColour(wx.Colour("PLUM"))
          label_118.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_5.Add(label_118, 0, wx.ALL | wx.EXPAND, 1)
          label_119 = wx.StaticText(
               self, wx.ID_ANY, "PURPLE", style=wx.ALIGN_CENTER)
          label_119.SetBackgroundColour(wx.Colour("PURPLE"))
          label_119.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_5.Add(label_119, 0, wx.ALL | wx.EXPAND, 1)
          sizer_2.Add(sizer_5, 1, wx.EXPAND, 0)
          label_120 = wx.StaticText(
               self, wx.ID_ANY, "RED", style=wx.ALIGN_CENTER)
          label_120.SetBackgroundColour(wx.Colour("RED"))
          label_120.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_6.Add(label_120, 0, wx.ALL | wx.EXPAND, 1)
          label_121 = wx.StaticText(
               self, wx.ID_ANY, "SALMON", style=wx.ALIGN_CENTER)
          label_121.SetBackgroundColour(wx.Colour("SALMON"))
          label_121.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_6.Add(label_121, 0, wx.ALL | wx.EXPAND, 1)
          label_122 = wx.StaticText(
               self, wx.ID_ANY, "SEA GREEN", style=wx.ALIGN_CENTER)
          label_122.SetBackgroundColour(wx.Colour("SEA GREEN"))
          label_122.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_6.Add(label_122, 0, wx.ALL | wx.EXPAND, 1)
          label_123 = wx.StaticText(
               self, wx.ID_ANY, "SIENNA", style=wx.ALIGN_CENTER)
          label_123.SetBackgroundColour(wx.Colour("SIENNA"))
          label_123.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_6.Add(label_123, 0, wx.ALL | wx.EXPAND, 1)
          label_124 = wx.StaticText(
               self, wx.ID_ANY, "SKY BLUE", style=wx.ALIGN_CENTER)
          label_124.SetBackgroundColour(wx.Colour("SKY BLUE"))
          label_124.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_6.Add(label_124, 0, wx.ALL | wx.EXPAND, 1)
          label_125 = wx.StaticText(
               self, wx.ID_ANY, "SLATE BLUE", style=wx.ALIGN_CENTER)
          label_125.SetBackgroundColour(wx.Colour("SLATE BLUE"))
          label_125.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_6.Add(label_125, 0, wx.ALL | wx.EXPAND, 1)
          label_126 = wx.StaticText(
               self, wx.ID_ANY, "SPRING GREEN", style=wx.ALIGN_CENTER)
          label_126.SetBackgroundColour(wx.Colour("SPRING GREEN"))
          label_126.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_6.Add(label_126, 0, wx.ALL | wx.EXPAND, 1)
          label_127 = wx.StaticText(
               self, wx.ID_ANY, "STEEL BLUE", style=wx.ALIGN_CENTER)
          label_127.SetBackgroundColour(wx.Colour("STEEL BLUE"))
          label_127.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_6.Add(label_127, 0, wx.ALL | wx.EXPAND, 1)
          label_128 = wx.StaticText(
               self, wx.ID_ANY, "TAN", style=wx.ALIGN_CENTER)
          label_128.SetBackgroundColour(wx.Colour("TAN"))
          label_128.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_6.Add(label_128, 0, wx.ALL | wx.EXPAND, 1)
          label_129 = wx.StaticText(
               self, wx.ID_ANY, "THISTLE", style=wx.ALIGN_CENTER)
          label_129.SetBackgroundColour(wx.Colour("THISTLE"))
          label_129.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_6.Add(label_129, 0, wx.ALL | wx.EXPAND, 1)
          label_130 = wx.StaticText(
               self, wx.ID_ANY, "TURQUOISE", style=wx.ALIGN_CENTER)
          label_130.SetBackgroundColour(wx.Colour("TURQUOISE"))
          label_130.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_6.Add(label_130, 0, wx.ALL | wx.EXPAND, 1)
          label_131 = wx.StaticText(
               self, wx.ID_ANY, "VIOLET", style=wx.ALIGN_CENTER)
          label_131.SetBackgroundColour(wx.Colour("VIOLET"))
          label_131.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_6.Add(label_131, 0, wx.ALL | wx.EXPAND, 1)
          label_132 = wx.StaticText(
               self, wx.ID_ANY, "VIOLET RED", style=wx.ALIGN_CENTER)
          label_132.SetBackgroundColour(wx.Colour("VIOLET RED"))
          label_132.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_6.Add(label_132, 0, wx.ALL | wx.EXPAND, 1)
          label_133 = wx.StaticText(
               self, wx.ID_ANY, "WHEAT", style=wx.ALIGN_CENTER)
          label_133.SetBackgroundColour(wx.Colour("WHEAT"))
          label_133.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_6.Add(label_133, 0, wx.ALL | wx.EXPAND, 1)
          label_134 = wx.StaticText(
               self, wx.ID_ANY, "WHITE", style=wx.ALIGN_CENTER)
          label_134.SetBackgroundColour(wx.Colour("WHITE"))
          label_134.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_6.Add(label_134, 0, wx.ALL | wx.EXPAND, 1)
          label_135 = wx.StaticText(
               self, wx.ID_ANY, "YELLOW", style=wx.ALIGN_CENTER)
          label_135.SetBackgroundColour(wx.Colour("YELLOW"))
          label_135.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_6.Add(label_135, 0, wx.ALL | wx.EXPAND, 1)
          label_136 = wx.StaticText(
               self, wx.ID_ANY, "YELLOW GREEN", style=wx.ALIGN_CENTER)
          label_136.SetBackgroundColour(wx.Colour("YELLOW GREEN"))
          label_136.SetForegroundColour(wx.Colour(0, 0, 0))
          sizer_6.Add(label_136, 0, wx.ALL | wx.EXPAND, 1)
          sizer_2.Add(sizer_6, 1, wx.EXPAND, 0)
          sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
          self.SetSizer(sizer_1)
          sizer_1.Fit(self)
          self.Layout()
          
# end of class MyFrame
class MyApp(wx.App):
     def OnInit(self):
          self.frame = MyFrame(None, wx.ID_ANY, "")
          self.SetTopWindow(self.frame)
          self.frame.Show()
          return True

# end of class MyApp
if __name__ == "__main__":
     app = MyApp(0)
     app.MainLoop()