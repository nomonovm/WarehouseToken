from rest_framework.generics import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class BolimListCreateView(ListCreateAPIView):
    def get_queryset(self):
        return Bolim.objects.all().order_by('nom')

    serializer_class = BolimSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]


class MahsulotListCreateView(ListCreateAPIView):
    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'sotuvchi') and user.sotuvchi.bolim:
            return Mahsulot.objects.filter(bolim=user.sotuvchi.bolim).order_by('nom')
        return Mahsulot.objects.none()

    serializer_class = MahsulotSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        if hasattr(user, 'sotuvchi') and user.sotuvchi.bolim:
            serializer.save(bolim=user.sotuvchi.bolim)
            serializer.save(sotuvchi=user)


class MahsulotRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'sotuvchi') and user.sotuvchi.bolim:
            return Mahsulot.objects.filter(bolim=user.sotuvchi.bolim).order_by('nom')
        return Mahsulot.objects.none()

    serializer_class = MahsulotSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        user = self.request.user
        if hasattr(user, 'sotuvchi') and user.sotuvchi.bolim:
            serializer.save(bolim=user.sotuvchi.bolim)
            serializer.save(sotuvchi=user)


class MijozListCreateView(ListCreateAPIView):
    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'sotuvchi') and user.sotuvchi.bolim:
            return Mijoz.objects.filter(bolim=user.sotuvchi.bolim).order_by('ism')
        return Mijoz.objects.none()

    serializer_class = MijozSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        if hasattr(user, 'sotuvchi') and user.sotuvchi.bolim:
            serializer.save(bolim=user.sotuvchi.bolim)
            serializer.save(sotuvchi=user)


class MijozRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'sotuvchi') and user.sotuvchi.bolim:
            return Mijoz.objects.filter(bolim=user.sotuvchi.bolim).order_by('ism')
        return Mijoz.objects.none()

    serializer_class = MijozSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        user = self.request.user
        if hasattr(user, 'sotuvchi') and user.sotuvchi.bolim:
            serializer.save(bolim=user.sotuvchi.bolim)
            serializer.save(sotuvchi=user)


class SotuvchiListCreateView(ListCreateAPIView):
    queryset = Sotuvchi.objects.all()
    serializer_class = SotuvchiSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class SotuvchiRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Sotuvchi.objects.all()
    serializer_class = SotuvchiSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class SotuvListCreateView(ListCreateAPIView):
    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'sotuvchi') and user.sotuvchi.bolim:
            return Sotuv.objects.filter(bolim=user.sotuvchi.bolim).order_by('nom')
        return Sotuv.objects.none()

    serializer_class = SotuvSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        if hasattr(user, 'sotuvchi') and user.sotuvchi.bolim:
            serializer.save(sotuvchi=user)
            serializer.save(bolim=user.sotuvchi.bolim)


class SotuvRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'sotuvchi') and user.sotuvchi.bolim:
            return Sotuv.objects.filter(bolim=user.sotuvchi.bolim).order_by('nom')
        return Sotuv.objects.none()

    serializer_class = SotuvSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        user = self.request.user
        if hasattr(user, 'sotuvchi') and user.sotuvchi.bolim:
            serializer.save(sotuvchi=user)
            serializer.save(bolim=user.sotuvchi.bolim)
