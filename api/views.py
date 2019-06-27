from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class GameOfThronesView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        message = '''To be fair, you have to have a very high IQ to understand game of thrones. The politics are extremely subtle, and without a solid grasp of the lore most of the magic will go over a typical viewer's head. There's also the hound's nihilistic outlook, which is deftly woven into his characterisation - his personal philosophy draws heavily from j.d. salinger’s literature, for instance. The fans understand this stuff; they have the intellectual capacity to truly appreciate the depths of the drama, to realize that they're not just suspense- they say something deep about LIFE. As a consequence people who dislike game of thrones truly ARE idiots- of course they wouldn't appreciate, for instance, the humour in house Stark's existencial catchphrase "whinter is coming," which itself is a cryptic reference to Turgenev's Russian epic Fathers and Sons I'm smirking right now just imagining one of those delapedated simpletons scratching their heads in confusion as Gerorge R R martin's genius unfolds itself on their television screens. What fools... how I pity them. :joy: And yes by the way, I DO have a Jon Snow tattoo. And no, you cannot see it. It's for the night’s watch eyes only- And even they have to demonstrate that they're within a similarly noble house of my own according to the “which Game of thrones house are you?” Facebook quiz (preferably lower) beforehand.'''
        content = {'message': message}
        return Response(content)
