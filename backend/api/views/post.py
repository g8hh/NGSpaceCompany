# -*- coding: utf-8 -*-

from api.views._base import *
        
        
        
################################################################################
class PostView(APIView):
    permission_classes = (IsAuthenticated, )
    
	#---------------------------------------------------------------------------
    def post(self, request):
        #-----------------------------------------------------------------------
        dbConnect()
        #-----------------------------------------------------------------------
        rank = request.data['rank']
        dbExecute("INSERT INTO ngsp_ranks(user_id, level, needed, remaining) VALUES(" + str(request.user.id) + "," + str(rank['level']) + "," + str(rank['xpNeeded']) + "," + str(rank['xpLeft']) + ")")
        #-----------------------------------------------------------------------
        return Response(request.data, status=status.HTTP_200_OK)
        #-----------------------------------------------------------------------
