menu = {

    'Beijing':{

        'Haidian':{

            'Wudaokou':{

                'soho':{},

                'Wangyi':{},

                'google':{}

            },

            'Zhongguancun':{

                'Aiqiyi':{},

                'Qichezhijia':{},

                'youku':{},

            },

            'Shangdi':{

                'Baidu':{},

            },

        },

        'Changping':{

            'Shahe':{

                'Laonanhai':{},

                'Beihang':{},

            },

            'Tiantongyuan':{},

            'Huilongguan':{},

        },

        'Chaoyang':{},

        'Dongcheng':{},

    },

    'Shanguhai':{

        'Minhang':{

            "Renminguangchang":{

                'Zhajidian':{}

            }

        },

        'Zhabei':{

            'Bus Station':{

                'Xiecheng':{}

            }

        },

        'Pudong':{},

    },

    'Shandong':{},

}
i=0 
record=[]
time=0
memory=menu

while menu!={}:
	for i in (menu):
		print (i)
		
	choice=input('Please input your destination：')
	if choice =='Exit':
		break
		
	elif choice =='Back':
		menu=memory
		del record[time-1]
		count=0
		while count<time-1:
			menu=menu.get(record[count])
			count+=1
		time=time-1
	
	elif choice in (menu):
		record.append(choice)
		menu=menu.get(choice)
		time+=1
		
