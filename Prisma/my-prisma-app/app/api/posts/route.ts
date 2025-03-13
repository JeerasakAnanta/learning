import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

/**
 * GET /api/posts
 * Retrieves a list of all posts
 * @returns A JSON response containing the list of posts
 */
export async function GET() {
  const posts = await prisma.post.findMany();

  return Response.json(posts);
}

export async function POST(request: Request) {
  const { title, content } = await request.json();
  // prisma  creat ORM
  const newPost = await prisma.post.create({
    data: { title, content },
  });
  return Response.json(newPost);
}