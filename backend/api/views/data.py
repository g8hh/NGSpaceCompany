# -*- coding: utf-8 -*-

from api.views._base import *
        
        
        
################################################################################
class RanksView(APIView):
    permission_classes = (AllowAny, )
    
	#---------------------------------------------------------------------------
    def get(self, request):
        #-----------------------------------------------------------------------
        dbConnect()
        #-----------------------------------------------------------------------
        data = dbRows("SELECT username, level, needed, remaining FROM ngsp_ranks JOIN auth_user ON ngsp_ranks.user_id = auth_user.id ORDER BY level DESC, remaining")
        #-----------------------------------------------------------------------
        return Response(data)
        #-----------------------------------------------------------------------
        
        
        
################################################################################
class StatsView(APIView):
    permission_classes = (AllowAny, )
    
	#---------------------------------------------------------------------------
    def get(self, request):
        #-----------------------------------------------------------------------
        dbConnect()
        #-----------------------------------------------------------------------
        data = dbRows("SELECT username, ultrite, enlightenment, darkmatter, rebirth, xp FROM ngsp_stats JOIN auth_user ON ngsp_stats.user_id = auth_user.id ORDER BY ultrite DESC, darkmatter DESC, xp DESC")
        #-----------------------------------------------------------------------
        return Response(data)
        #-----------------------------------------------------------------------