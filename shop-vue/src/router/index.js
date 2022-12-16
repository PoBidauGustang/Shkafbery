import { createRouter, createWebHashHistory } from "vue-router";
import HomePage from "../views/home_page/HomePage.vue";
import store from "../store/index.js";

const routes = [
  {
    path: "/",
    name: "HomePage",
    component: HomePage,
  },
  {
    path: "/login",
    name: "Login",
    component: () => import("../components/TheAuth/TheLogin.vue"),
  },
  {
    path: "/register",
    name: "Register",
    component: () => import("../components/TheAuth/TheRegister.vue"),
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: () => import("../views/Dashboard.vue"),
    meta: {
      requiresAuth: true,
    },
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
    path: "/product/:id",
    name: "product",
    component: () => import("../views/products/ProductPage.vue"),
  },
  {
    path: "/category/:slug",
    name: "category",
    component: () => import("../views/products/Category.vue"),
  },
  {
    path: "/closet_planner",
    name: "ClosetPlanner",
    component: () => import("../views/PlannerCloset.vue"),
  },
  {
    path: "/measurements",
    name: "Measurements",
    component: () => import("../views/common_services/Measurements.vue"),
  },
  {
    path: "/installation",
    name: "Installation",
    component: () => import("../views/common_services/Installation.vue"),
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

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (store.getters["auth/ISLOGGEDIN"]) {
      next();
      return;
    }
    next("/login");
  } else {
    next();
  }
});

export default router;
