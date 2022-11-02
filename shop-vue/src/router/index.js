import { createRouter, createWebHashHistory } from "vue-router";
import HomePage from "../views/home_page/HomePage.vue";

const routes = [
  {
    path: "/",
    name: "HomePage",
    component: HomePage,
  },
  {
    path: "/login",
    name: "Login",
    component: () => import("../components/TheLogin.vue"),
  },
  {
    path: "/about",
    name: "about",
    component: () => import("../views/AboutPage.vue"),
  },
  {
    path: "/contacts",
    name: "contacs",
    component: () => import("../views/ContactPage.vue"),
  },
  {
    path: "/photos",
    name: "photos",
    component: () => import("../views/PhotosPage.vue"),
  },
  {
    path: "/partners",
    name: "PartnerPage",
    component: () => import("../views/PartnerPage.vue"),
  },
  {
    path: "/services",
    name: "ServicesPage",
    component: () => import("../views/ServicesPage.vue"),
  },
  {
    path: "/posts",
    name: "BlogPosts",
    component: () => import("../views/PostsPage.vue"),
  },
  {
    path: "/post/:slug",
    name: "article",
    component: () => import("../views/PostPageSingle.vue"),
  },
  {
    path: "/products",
    name: "Products",
    component: () => import("../views/products/Products.vue"),
  },
  {
    path: "/product/:id",
    name: "product",
    component: () => import("../views/ProductPageSingle.vue"),
  },
  {
    path: "/materials",
    name: "List materials",
    component: () => import("../views/MaterialsPage.vue"),
  },
  {
    path: "/material/:id",
    name: "materials",
    component: () => import("../views/MaterialPageSingle.vue"),
  },
  {
    path: "/accessories",
    name: "Accessories",
    component: () => import("../views/accessories/Accessories.vue"),
  },
  {
    path: "/kitchen",
    name: "kitchen",
    component: () => import("../views/KitchenPage.vue"),
  },
  {
    path: "/wardrobe",
    name: "wardrobe",
    component: () => import("../views/WardrobePage.vue"),
  },
  {
    path: "/closets",
    name: "Closets",
    component: () => import("../views/Closets.vue"),
  },
  {
    path: "/freestanding_closets",
    name: "FreestandingClosets",
    component: () => import("../views/FreestandingClosets.vue"),
  },
  {
    path: "/built-in_closets",
    name: "Built-inClosets",
    component: () => import("../views/Built-inClosets.vue"),
  },
  {
    path: "/closet_planner",
    name: "ClosetPlanner",
    component: () => import("../views/PlannerCloset.vue"),
  },
  {
    path: "/doors_closet",
    name: "DoorsCloset",
    component: () => import("../views/doors/DoorsCloset.vue"),
  },
  {
    path: "/doors_opening",
    name: "DoorsTheOpening",
    component: () => import("../views/doors/DoorsTheOpening.vue"),
  },
  {
    path: "/doors_dressing_room",
    name: "DoorsDressingRoom",
    component: () => import("../views/doors/DoorsDressingRoom.vue"),
  },
  {
    path: "/cutting",
    name: "Cutting",
    component: () => import("../views/services/Cutting.vue"),
  },
  {
    path: "/measurements",
    name: "Measurements",
    component: () => import("../views/services/Measurements.vue"),
  },
  {
    path: "/installation",
    name: "Installation",
    component: () => import("../views/services/Installation.vue"),
  },
  {
    path: "/chipboard",
    name: "Chipboard",
    component: () => import("../views/materials/Chipboard.vue"),
  },
  {
    path: "/mirror",
    name: "Mirror",
    component: () => import("../views/materials/Mirror.vue"),
  },
  {
    path: "/other",
    name: "Other",
    component: () => import("../views/materials/Other.vue"),
  },
  {
    path: "/cart",
    name: "TheCart",
    component: () => import("../views/cart/TheCart.vue"),
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
